"use client";

import { useRef, useState } from "react";

/**
 * Lazy audio player — only downloads the audio file when the user clicks play.
 * Saves bandwidth vs. <audio src={url}> which preloads immediately.
 */
export function LazyAudio({ src, className }: { src: string; className?: string }) {
  const [loaded, setLoaded] = useState(false);
  const audioRef = useRef<HTMLAudioElement>(null);

  function handlePlay() {
    if (!loaded) {
      setLoaded(true);
      // After state update, the src is set and we need to play
      setTimeout(() => {
        audioRef.current?.play().catch(() => {});
      }, 0);
    }
  }

  return (
    <audio
      ref={audioRef}
      controls
      src={loaded ? src : undefined}
      onPlay={!loaded ? handlePlay : undefined}
      className={className ?? "w-full h-9"}
      preload="none"
    />
  );
}
