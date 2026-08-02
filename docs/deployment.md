# Deployment & Production Setup Guide

## Overview
This document outlines production deployment strategies for the IELTS AI Speaking Classroom, including Supabase configuration, Next.js frontend hosting, and FastAPI backend hosting.

---

## 1. Supabase Infrastructure Setup

### Database & Realtime
1. Create a project at [Supabase Dashboard](https://supabase.com/dashboard).
2. Execute initial SQL schema migrations (`migrations/01_schema.sql` or equivalent):
   - Tables: `users`, `rooms`, `participants`, `questions`, `answers`, `evaluations`.
3. Enable Supabase Realtime publication for live room tables:
   ```sql
   alter publication supabase_realtime add table public.rooms, public.participants;
   ```

### Storage Bucket & Security (RLS)
1. Create a bucket named `audio` in Supabase Storage.
2. Configure bucket settings to **Public**.
3. Apply Row Level Security (RLS) policies on `storage.objects`:
   ```sql
   -- Allow authenticated users to upload audio files
   CREATE POLICY "authenticated_upload" ON storage.objects
   FOR INSERT TO authenticated
   WITH CHECK (bucket_id = 'audio');

   -- Allow authenticated users to read audio files
   CREATE POLICY "authenticated_read" ON storage.objects
   FOR SELECT TO authenticated
   USING (bucket_id = 'audio');
   ```

---

## 2. Backend Deployment (FastAPI)

### Recommended Platforms
- **Render**, **Fly.io**, **Railway**, or **AWS ECS / App Runner**.

### Environment Variables
Configure the following environment variables in your deployment dashboard:
```env
SUPABASE_URL=https://<your-project-ref>.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
SUPABASE_ANON_KEY=your-anon-key
GEMINI_API_KEY=your-gemini-api-key
GEMINI_EVAL_MODEL=gemini-3.5-flash
```

### Production Dockerfile Example
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 3. Frontend Deployment (Next.js 15)

### Recommended Platforms
- **Vercel** or **Netlify**.

### Build Command & Settings
- **Framework Preset**: Next.js
- **Build Command**: `npm run build`
- **Output Directory**: `.next`

### Environment Variables
```env
NEXT_PUBLIC_SUPABASE_URL=https://<your-project-ref>.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
NEXT_PUBLIC_API_URL=https://your-backend-api.onrender.com
```

---

## 4. Verification Checklist
- [ ] Next.js app builds cleanly (`npm run build`).
- [ ] Backend health check `GET /api/health` returns `{"status": "ok"}`.
- [ ] RLS policies enable students to upload `.webm`/`.mp4` recordings.
- [ ] Supabase Realtime channel connections succeed over WebSockets (`wss://`).
- [ ] Audio playback URL is accessible via HTTPS on student reports.
