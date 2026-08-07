"""Writing Task 2 practice questions and sample answers.

Contains 24 IELTS Writing Task 2 essay questions across 6 essay types
(4 per type), each with 3 model answers (Band 5, 7, 9). Topics are real
IELTS-style but written to be approachable for practice.

Each sample includes sub-scores, an explanation of why it is at that band,
and specific improvement tips.
"""

from __future__ import annotations

PART = 2

# ---------------------------------------------------------------------------
# Questions
# ---------------------------------------------------------------------------

QUESTIONS: list[dict] = [
    # ---------- OPINION (4) ----------
    {
        "type": "opinion",
        "title": "Some people think children should start school earlier",
        "difficulty": "easy",
        "prompt": (
            "Some people believe that children should start school as early as possible, "
            "while others think they should stay at home until they are older.\n\n"
            "To what extent do you agree or disagree that children should begin formal "
            "education at a very young age?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "opinion",
        "title": "Paying teachers according to student results",
        "difficulty": "medium",
        "prompt": (
            "Some people argue that teachers should be paid according to how well their "
            "students perform in exams.\n\n"
            "To what extent do you agree or disagree?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "opinion",
        "title": "Money is the most important thing in life",
        "difficulty": "easy",
        "prompt": (
            "Some people say that money is the most important thing in life.\n\n"
            "To what extent do you agree or disagree with this opinion?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "opinion",
        "title": "Mobile phones should be banned in schools",
        "difficulty": "medium",
        "prompt": (
            "Some people believe that mobile phones should be completely banned in schools, "
            "while others think they can be useful for learning.\n\n"
            "To what extent do you agree or disagree with banning mobile phones in schools?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    # ---------- DISCUSSION (4) ----------
    {
        "type": "discussion",
        "title": "Working from home vs. working in an office",
        "difficulty": "easy",
        "prompt": (
            "More and more people are choosing to work from home rather than travel to an "
            "office every day.\n\n"
            "Some people believe working from home is better for everyone, while others think "
            "working in an office is still preferable.\n\n"
            "Discuss both views and give your own opinion.\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "discussion",
        "title": "Wild animals should or should not be kept in zoos",
        "difficulty": "easy",
        "prompt": (
            "Many cities have zoos that keep wild animals in cages or large enclosures.\n\n"
            "Some people think zoos are cruel and should be closed down, while others believe "
            "they help protect endangered species.\n\n"
            "Discuss both views and give your own opinion.\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "discussion",
        "title": "Children should or should not do housework",
        "difficulty": "easy",
        "prompt": (
            "Some parents believe children should help with housework, such as cleaning and "
            "cooking, while others think children should focus only on their studies.\n\n"
            "Discuss both views and give your own opinion.\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "discussion",
        "title": "Advertising encourages or discourages buying",
        "difficulty": "medium",
        "prompt": (
            "Advertising is everywhere: on television, the internet, and the streets.\n\n"
            "Some people say advertising helps people make better buying decisions, while "
            "others claim it encourages people to buy things they do not need.\n\n"
            "Discuss both views and give your own opinion.\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    # ---------- ADVANTAGES & DISADVANTAGES (4) ----------
    {
        "type": "advantages",
        "title": "Living in a big city",
        "difficulty": "easy",
        "prompt": (
            "An increasing number of people are moving from the countryside to live in big "
            "cities.\n\n"
            "What are the advantages and disadvantages of living in a big city?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "advantages",
        "title": "Using public transport instead of cars",
        "difficulty": "medium",
        "prompt": (
            "Many governments are encouraging people to use public transport instead of "
            "private cars.\n\n"
            "What are the advantages and disadvantages of using public transport?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "advantages",
        "title": "Studying abroad",
        "difficulty": "easy",
        "prompt": (
            "More students than ever before are choosing to study at universities in another "
            "country.\n\n"
            "What are the advantages and disadvantages of studying abroad?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "advantages",
        "title": "Using social media for news",
        "difficulty": "medium",
        "prompt": (
            "Nowadays many people get their daily news from social media platforms instead "
            "of traditional newspapers and television.\n\n"
            "What are the advantages and disadvantages of getting news from social media?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    # ---------- PROBLEM & SOLUTION (4) ----------
    {
        "type": "problem_solution",
        "title": "Traffic congestion in big cities",
        "difficulty": "easy",
        "prompt": (
            "Traffic congestion has become a serious problem in many big cities around the "
            "world.\n\n"
            "What are the causes of this problem, and what solutions can governments and "
            "individuals take to solve it?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "problem_solution",
        "title": "Rising obesity among young people",
        "difficulty": "easy",
        "prompt": (
            "Obesity is increasing among young people in many countries.\n\n"
            "What problems does this cause, and what measures could be taken to encourage "
            "young people to be more active and eat more healthily?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "problem_solution",
        "title": "Plastic waste harming the environment",
        "difficulty": "medium",
        "prompt": (
            "Plastic waste is causing serious damage to the environment, especially in oceans "
            "and rivers.\n\n"
            "What problems does plastic pollution create, and what solutions can governments, "
            "companies, and individuals adopt to reduce it?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "problem_solution",
        "title": "Young people not choosing science careers",
        "difficulty": "medium",
        "prompt": (
            "In many countries, fewer young people are choosing to study science and "
            "technology subjects at university.\n\n"
            "What problems can this cause for society, and what steps could be taken to "
            "encourage more young people to study science?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    # ---------- POSITIVE / NEGATIVE DEVELOPMENT (4) ----------
    {
        "type": "positive_negative",
        "title": "Online shopping replacing high streets",
        "difficulty": "easy",
        "prompt": (
            "Online shopping has grown rapidly, and many traditional shops on the high street "
            "have closed down.\n\n"
            "Is this a positive or negative development?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "positive_negative",
        "title": "People living longer than ever before",
        "difficulty": "medium",
        "prompt": (
            "Thanks to better healthcare and living standards, people today live much longer "
            "than people did in the past.\n\n"
            "Is this a positive or negative development?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "positive_negative",
        "title": "Learning English as a global language",
        "difficulty": "easy",
        "prompt": (
            "English is now studied as a second language by millions of people around the "
            "world.\n\n"
            "Is the spread of English as a global language a positive or negative "
            "development?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "positive_negative",
        "title": "Automation replacing human jobs",
        "difficulty": "hard",
        "prompt": (
            "Machines and computers are increasingly able to do jobs that used to be done by "
            "people.\n\n"
            "Is this a positive or negative development?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    # ---------- DOUBLE QUESTION (4) ----------
    {
        "type": "double_question",
        "title": "Fast food popularity among young people",
        "difficulty": "easy",
        "prompt": (
            "Fast food restaurants have become very popular with young people all over the "
            "world.\n\n"
            "Why do you think fast food is so popular with young people?\n"
            "What measures could be taken to encourage them to eat more healthily?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "double_question",
        "title": "Rise of remote learning",
        "difficulty": "medium",
        "prompt": (
            "In recent years, more students have been learning online rather than in "
            "traditional classrooms.\n\n"
            "Why has online learning become so popular?\n"
            "What are the effects of this trend on students and teachers?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "double_question",
        "title": "International travel growth",
        "difficulty": "easy",
        "prompt": (
            "International travel has become easier and cheaper than ever before, and more "
            "people are visiting foreign countries.\n\n"
            "Why do you think more people are travelling abroad nowadays?\n"
            "What effects does international travel have on the countries people visit?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
    {
        "type": "double_question",
        "title": "Teenagers and part-time jobs",
        "difficulty": "medium",
        "prompt": (
            "In many countries, teenagers take part-time jobs during weekends and school "
            "holidays.\n\n"
            "Why do many teenagers choose to work part-time?\n"
            "What are the advantages and possible risks of doing so?\n\n"
            "Give reasons for your answer and include any relevant examples from your own "
            "knowledge or experience.\n\n"
            "Write at least 250 words."
        ),
    },
]


# ---------------------------------------------------------------------------
# Sample answers. Keyed by question index -> {band: sample}
# ---------------------------------------------------------------------------

SAMPLES: dict[int, dict[str, dict]] = {
    # ---------------- Q0: Children start school early (opinion) ----------------
    0: {
        "5": {
            "band": 5,
            "answer_text": (
                "Nowadays many parents want their children to start school early. I think it is good "
                "because children can learn many things at school.\n"
                "When children go to school early, they can learn to read and write before they are "
                "too old. For example, my cousin started school when he was four years old, and now he "
                "is very good at reading. Also, at school children can meet other children and make "
                "friends. They can play together and learn to share things.\n"
                "However, there is also one bad thing about starting school early. Small children may "
                "feel tired because school is every day. They may miss their mother and father. In my "
                "opinion, starting school at a young age is mostly good, but parents should be careful "
                "that their children are happy.\n"
                "To conclude, I believe children should start school early, but it is also important "
                "for them to have time to play at home with their family."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The answer gives a clear opinion and some reasons, but the paragraphs are simple and "
                "the examples are personal and undeveloped. The vocabulary is basic and there are "
                "repetitive sentence structures. The position is clear but the argument is not fully "
                "extended."
            ),
            "improvement_tips": [
                "Develop each idea in a full paragraph with a topic sentence and supporting detail.",
                "Use linking words such as 'moreover', 'in addition' and 'on the other hand'.",
                "Replace simple vocabulary ('good', 'bad') with more precise words such as 'beneficial' and 'disadvantageous'.",
                "Include a clear opinion statement in the introduction.",
                "Reduce repetition of 'children' and 'school' by using synonyms.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Whether children should begin formal education at a very young age is a question that "
                "divides parents and educators. While I recognise the benefits of early schooling, I "
                "believe it depends on the individual child, and that a very early start is not always "
                "the best option.\n"
                "On the one hand, starting school early can bring clear academic advantages. Children "
                "who learn to read and count from the age of four or five often develop these skills "
                "more quickly. In many countries, early education has been shown to improve later "
                "performance at primary school. Furthermore, school helps young children socialise; "
                "they learn to share, cooperate and follow instructions in a group, which prepares "
                "them for adult life.\n"
                "On the other hand, very young children may not be emotionally ready for the demands "
                "of formal education. Long school days can cause tiredness and stress, and some "
                "children may struggle to be separated from their parents for long periods. This is "
                "especially true for children who are naturally shy or who develop slowly. In such "
                "cases, an extra year at home with family can be far more beneficial than an early "
                "start at school.\n"
                "In conclusion, although early schooling offers academic and social benefits, I do not "
                "believe every child should start school as soon as possible. Parents should consider "
                "each child's maturity and readiness before making this important decision."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response presents a clear, balanced position and develops two well-organised "
                "paragraphs with supporting ideas. Cohesive devices are used effectively, and the "
                "vocabulary is appropriate, though a little more sophistication and precision would "
                "lift it to a higher band. Grammar is largely accurate."
            ),
            "improvement_tips": [
                "Add more specific and varied examples to strengthen the arguments.",
                "Use more advanced collocations such as 'cognitive development' or 'emotional readiness'.",
                "Vary sentence beginnings to improve flow.",
                "Make the conclusion more decisive by restating the position with fresh wording.",
                "Introduce a concessive sentence ('Even so...') to add depth.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The age at which children should begin formal schooling is a subject of considerable "
                "debate among parents and education specialists. While there are undeniable benefits to "
                "an early start, I would argue that formal education should not be forced on the very "
                "young, as each child develops at his or her own pace.\n"
                "There is little doubt that early schooling can accelerate academic progress. Children "
                "who are introduced to literacy and numeracy at four or five often acquire these "
                "foundational skills with remarkable ease, and longitudinal studies suggest that early "
                "intervention can have a lasting impact on later achievement. Moreover, the school "
                "environment offers an invaluable opportunity for social development; within a group "
                "of peers, children learn to negotiate, cooperate and resolve conflicts, competencies "
                "that cannot easily be acquired in isolation at home.\n"
                "Nevertheless, the psychological readiness of a young child must not be overlooked. The "
                "rigid routines and cognitive demands of a formal curriculum can prove overwhelming for "
                "children who are not yet emotionally equipped to cope, leading to anxiety and a "
                "dislike of learning that may persist for years. Indeed, a significant body of research "
                "indicates that overly early formal instruction can be counterproductive, whereas "
                "play-based learning at home or in a nursery setting more closely matches the "
                "developmental needs of younger children.\n"
                "In conclusion, while early education confers clear academic and social advantages, it "
                "should not be regarded as universally beneficial. A more judicious approach is to "
                "allow children to begin formal schooling when they are developmentally ready, rather "
                "than imposing a single age on all."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay fully addresses the question with a clear, sustained position developed "
                "throughout. Ideas are logically organised and skilfully linked using a wide range of "
                "cohesive devices. The vocabulary is sophisticated and precise, and the grammatical "
                "structures are varied and consistently accurate."
            ),
            "improvement_tips": [
                "The response is already at a high level; maintain the balance between paragraphs.",
                "Consider adding one concrete real-world example to anchor the second argument.",
                "Avoid any temptation to overcomplicate vocabulary where clarity is already strong.",
            ],
        },
    },
    # ---------------- Q1: Paying teachers by results (opinion) ----------------
    1: {
        "5": {
            "band": 5,
            "answer_text": (
                "Some people think teachers should get more money if their students do well in exams. "
                "I do not agree with this idea because it is not fair for all teachers.\n"
                "If teachers are paid by results, teachers in rich schools will get more money, because "
                "students in these schools are easy to teach. But teachers in poor areas work very hard "
                "with students who have many problems, and they will get less money. This is not fair.\n"
                "Also, if teachers think only about exams, they may not teach other important things "
                "like art, music, or good manners. Students need to learn many things, not only for "
                "exams.\n"
                "I think teachers should be paid the same salary, and if they are good, they can get a "
                "bonus. In this way, teachers will be happy and students will learn better.\n"
                "In conclusion, paying teachers according to exam results is a bad idea, and I believe "
                "all teachers should be treated the same."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "A clear opinion is given and a reasonable number of ideas are presented. However, the "
                "paragraphs are short, development is limited, and the vocabulary and grammar are "
                "simple with some repetition. There is an attempt at a conclusion."
            ),
            "improvement_tips": [
                "Develop each point in a full paragraph instead of several short ones.",
                "Add an example to support the claim about teachers in poor areas.",
                "Use connectors such as 'furthermore' and 'consequently'.",
                "Improve grammar accuracy, for example 'if teachers are paid by results'.",
                "Expand the conclusion to summarise the main reasons clearly.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The idea of linking teachers' salaries to their students' exam performance is becoming "
                "increasingly popular in some countries. In my view, this approach is misguided, because "
                "it fails to account for the many factors that influence a student's results.\n"
                "Those who support performance-related pay argue that it motivates teachers to work "
                "harder and to focus on raising standards. In theory, this sounds attractive: if teachers "
                "are rewarded for success, they may plan lessons more carefully and give students extra "
                "support. However, in practice, the system is deeply unfair. A teacher in a school where "
                "students come from wealthy, supportive homes will almost certainly achieve better "
                "results than a colleague in an underprivileged area, regardless of the quality of their "
                "teaching.\n"
                "Furthermore, performance-related pay encourages a narrow focus on exam preparation. "
                "When salaries depend on test scores, teachers may be tempted to 'teach to the test' and "
                "neglect broader skills such as creativity, critical thinking and teamwork, which are "
                "equally important for a child's development.\n"
                "In conclusion, I strongly disagree with paying teachers according to their students' "
                "exam results. A fairer approach would be to reward teachers based on professional "
                "qualifications, experience and consistent performance, rather than on results that are "
                "largely influenced by factors beyond their control."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay gives a clear position and develops the argument in a logical sequence, with "
                "a counterargument acknowledged and refuted. The vocabulary is varied and mostly "
                "accurate, and cohesion is managed well. It lacks a fully convincing, specific example "
                "and occasional idiomatic phrasing."
            ),
            "improvement_tips": [
                "Include a specific example (e.g., a country that tried the system) to strengthen the argument.",
                "Use more advanced linking phrases such as 'this contention rests on the assumption that...'.",
                "Add a sentence with an emphatic structure or a cleft sentence for variety.",
                "Ensure the conclusion synthesises rather than repeats the introduction.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The proposition that teachers' remuneration should be tied to their students' examination "
                "results has gained traction in several education systems. While the rationale behind such "
                "a policy is superficially appealing, I am firmly of the opinion that it is fundamentally "
                "flawed and would do more harm than good.\n"
                "Proponents of performance-related pay contend that it creates a powerful incentive for "
                "teachers to raise attainment. They point to the business world, where bonuses tied to "
                "output are believed to boost productivity. Yet this analogy collapses under scrutiny, for "
                "the simple reason that a child's academic success is shaped by a host of factors beyond "
                "the classroom: parental involvement, socioeconomic background, and even health. Two "
                "teachers of equal skill, placed in vastly different communities, would be rewarded "
                "unequally through no fault of their own, undermining morale and driving talented "
                "professionals away from the schools that need them most.\n"
                "Moreover, such a policy would inevitably distort educational priorities. When career "
                "progression hinges on test scores, the curriculum narrows: subjects and skills that are "
                "not readily measured are marginalised, and teaching degenerates into coaching for "
                "examinations. The result is a generation of students who can perform in tests but who "
                "lack the curiosity, creativity and resilience that genuine education is meant to foster.\n"
                "In conclusion, the notion of rewarding teachers according to exam results rests on a "
                "misunderstanding of what drives educational success. I would therefore contend that "
                "salaries should be determined by qualifications, experience and sustained professional "
                "merit, and that any attempt to tie pay to student outcomes should be rejected outright."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay presents a fully developed position with sophisticated, nuanced arguments. "
                "The business-world analogy is effectively dismantled, and the consequences are explored "
                "with precision. Cohesion is seamless, the lexical range is impressive, and grammatical "
                "structures are complex and consistently accurate."
            ),
            "improvement_tips": [
                "This response is at band 9 level; retain the precise use of concession and refutation.",
                "Consider a brief nod to a possible counter-rebuttal in the second paragraph for balance.",
            ],
        },
    },
    # ---------------- Q2: Money is the most important thing (opinion) ----------------
    2: {
        "5": {
            "band": 5,
            "answer_text": (
                "Some people think money is the most important thing in life. I do not agree, because "
                "money cannot buy health, family and friends.\n"
                "Of course, money is very important. We need money to buy food, clothes and a house. "
                "Without money, life is very difficult. For example, people without money cannot go to "
                "the doctor when they are sick.\n"
                "But there are many important things that money cannot buy. If a person is sick, money "
                "cannot always make him healthy. Also, a rich person can be very lonely if he has no "
                "friends. My grandfather says that time with family is the best present in the world.\n"
                "I think health and happiness are more important than money. Money can help us, but it "
                "is not the most important thing.\n"
                "In conclusion, money is useful, but family, health and friends are more important in "
                "life."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response states a clear opinion and provides relevant reasons. The structure is "
                "simple and the ideas are expressed in basic language with limited range. Personal "
                "anecdotes are used but not developed. Grammar is mostly simple sentences."
            ),
            "improvement_tips": [
                "Organise the body into two clear, developed paragraphs.",
                "Replace 'important' with stronger vocabulary such as 'essential' or 'indispensable'.",
                "Use conditionals correctly ('If a person is sick, money cannot always make him healthy').",
                "Add a clearer topic sentence to each paragraph.",
                "Link the conclusion to the main reasons you gave.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "There is a common belief that money is the most important thing in life. While I accept "
                "that financial security plays a vital role in modern living, I strongly disagree that it "
                "outweighs all other considerations such as health, relationships and happiness.\n"
                "It is undeniable that money matters a great deal. Without it, people struggle to afford "
                "basic necessities such as food, housing and medical care, and poverty can lead to stress "
                "and illness. Financial resources also open doors to education and opportunity, which is "
                "why many parents work so hard to provide for their children. In this sense, money is a "
                "necessary foundation for a decent standard of living.\n"
                "However, money alone cannot guarantee wellbeing. Good health, for example, is arguably "
                "more valuable; no amount of wealth can restore it once it is lost. Similarly, loving "
                "relationships with family and friends provide emotional support that money cannot buy. "
                "There are countless examples of wealthy individuals who lead unhappy, lonely lives, "
                "which suggests that true satisfaction comes from more than financial success.\n"
                "In conclusion, although money is undeniably important, I believe it is a means to an end "
                "rather than an end in itself. Health, relationships and personal fulfilment deserve "
                "greater value in a meaningful life."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay presents a balanced and clearly organised argument. The importance of money "
                "is acknowledged before being qualified, and the counterarguments are handled well. "
                "Cohesive devices and vocabulary are appropriate, though occasionally the ideas could be "
                "developed in greater depth."
            ),
            "improvement_tips": [
                "Develop the example of wealthy but unhappy individuals with more concrete detail.",
                "Use more sophisticated vocabulary such as 'materialistic', 'wellbeing' and 'fulfilment' in context.",
                "Introduce a wider range of grammatical structures, such as inversion or complex participles.",
                "Make the final sentence more impactful.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "A prevailing assumption in consumer societies is that money constitutes the most "
                "important element of a successful life. Although I concede that financial resources are "
                "indispensable to modern existence, I would maintain that this view is reductive, "
                "overlooking the deeper dimensions of human flourishing.\n"
                "There can be no disputing the practical importance of money. It secures shelter, "
                "sustenance and healthcare, and it affords access to education and opportunity. In "
                "societies where basic needs are unmet, the absence of money precipitates real suffering, "
                "and financial stability is rightly pursued with urgency. Indeed, for those living in "
                "poverty, the sentiment that 'money cannot buy happiness' rings hollow, since wealth can "
                "buy freedom from many of life's most pressing anxieties.\n"
                "Yet to elevate money to the status of life's foremost concern is to misunderstand the "
                "sources of human satisfaction. Health, for instance, is a precondition for the "
                "enjoyment of almost everything wealth provides, and no fortune can compensate for its "
                "loss. Likewise, the bonds of family and friendship, the pursuit of meaningful work, and "
                "the capacity for generosity all contribute to wellbeing in ways that money, however "
                "abundant, cannot purchase. Empirical studies repeatedly show that beyond a certain "
                "threshold, additional income yields diminishing returns in terms of reported happiness, "
                "while strong relationships remain one of the strongest predictors of life satisfaction.\n"
                "In conclusion, while money is an essential instrument in the pursuit of a comfortable "
                "life, it is not, and should not be, the measure of one's life. A life well lived is "
                "defined by health, connection and purpose, values that no bank balance can replace."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay is a model of clarity and depth: a clear position is argued with nuance, "
                "acknowledging both sides before reaching a considered conclusion. The vocabulary is "
                "precise and varied, cohesion is seamless, and complex grammatical structures are "
                "handled with complete accuracy."
            ),
            "improvement_tips": [
                "No significant improvement needed; this is a band 9 response.",
                "If desired, add a brief real-life anecdote, though the academic register is already appropriate.",
            ],
        },
    },
    # ---------------- Q3: Banning mobile phones in schools (opinion) ----------------
    3: {
        "5": {
            "band": 5,
            "answer_text": (
                "Mobile phones are very common now, and many students take them to school. Some people "
                "think phones should be banned in schools. I partly agree with this idea.\n"
                "Phones can make problems in class. Students use them to play games and chat with "
                "friends instead of listening to the teacher. For example, in my school, many students "
                "look at their phones during lessons, and their marks are not good.\n"
                "But phones are also useful. Students can use them to search for information for their "
                "projects, and parents can call their children after school. Some schools use phones "
                "for learning games, which students enjoy.\n"
                "I think phones should not be allowed during lessons, but students can use them at "
                "lunchtime. In this way, students will pay attention in class and still have their "
                "phones for other things.\n"
                "In conclusion, banning phones completely is not a good idea, but schools should make "
                "rules about when they can be used."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "A clear partial position is presented and supported with a relevant personal example. "
                "The response has a logical order but the language is basic, with simple structures and "
                "some repetition. The conclusion restates the position effectively."
            ),
            "improvement_tips": [
                "Write fuller paragraphs with a topic sentence and more supporting detail.",
                "Use more precise vocabulary such as 'distraction', 'educational resource' and 'restriction'.",
                "Vary sentence openings to avoid repetitive 'Phones...' beginnings.",
                "Use linking phrases like 'on the one hand' and 'on the other hand'.",
                "Proofread for minor errors such as article usage.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The widespread use of mobile phones has prompted many schools to consider banning them "
                "altogether. While I understand the concerns that lead to this demand, I believe that a "
                "total ban is unnecessary, and that sensible regulation is a better solution.\n"
                "Those who advocate a ban point out that phones are a major source of distraction in the "
                "classroom. Students who check messages or play games during lessons lose concentration, "
                "and this can affect not only their own learning but also the teacher's ability to manage "
                "the class. Moreover, phones can be used for cyberbullying, which is a serious problem in "
                "many schools.\n"
                "Nevertheless, mobile phones are also valuable educational tools. They provide instant "
                "access to information, allowing students to research topics during lessons, and many "
                "schools already use educational apps that support learning. Furthermore, phones give "
                "parents a way to stay in contact with their children, which is particularly important "
                "for safety after school hours.\n"
                "In my view, the answer is not to ban phones but to manage them carefully. Schools could "
                "require students to switch phones off during lessons while permitting their use at "
                "break times. Such a policy would minimise distractions while retaining the clear "
                "benefits that phones offer.\n"
                "In conclusion, I disagree with a complete ban on mobile phones in schools. A balanced "
                "policy of responsible use seems far more sensible than prohibition."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay takes a clear, balanced position and supports it with well-organised "
                "paragraphs. Both sides of the argument are presented fairly, and a practical compromise "
                "is proposed. Cohesion is effective and the language is accurate, though it could be more "
                "sophisticated in places."
            ),
            "improvement_tips": [
                "Provide a more concrete example to illustrate the value of phones in lessons.",
                "Use more advanced phrases such as 'a complete prohibition' or 'curtail the risks'.",
                "Vary sentence length for greater rhythm.",
                "Tighten the conclusion so it summarises the compromise clearly.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "As smartphones have become ubiquitous, schools worldwide have grappled with whether to "
                "prohibit their use outright. Although the concerns motivating such bans are entirely "
                "legitimate, I would argue that a blanket prohibition is a blunt instrument that ignores "
                "the genuine pedagogical value these devices can offer.\n"
                "The case for banning phones is a strong one. In the classroom, the constant temptation "
                "to check notifications erodes attention and undermines the quality of instruction; "
                "indeed, studies have linked smartphone use in lessons to measurably lower academic "
                "performance. There is also the darker dimension of cyberbullying, which flourishes when "
                "devices are always at hand, creating a school environment where some students feel "
                "unsafe. For many teachers, the simplest response to these problems is to remove the "
                "source altogether.\n"
                "Yet to banish phones is to forfeit their potential as instruments of learning. A "
                "well-managed classroom can deploy phones for research, collaborative projects and "
                "educational applications that would otherwise require expensive equipment. Furthermore, "
                "schooling that models the responsible use of technology arguably prepares students "
                "better for a digital world in which self-regulation, not avoidance, is the key skill. "
                "The challenge, therefore, is not whether phones should exist in schools, but how their "
                "use can be governed effectively.\n"
                "In conclusion, while the instinct to ban mobile phones is understandable, I contend that "
                "a considered policy of regulated use is both more realistic and more beneficial. Schools "
                "should teach students to manage technology responsibly rather than simply forbid it."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay fully addresses the question with a nuanced position sustained throughout. "
                "Arguments are developed with precision and supported by credible references to studies. "
                "The vocabulary is sophisticated, cohesion is seamless, and the grammatical range is "
                "wide and accurate."
            ),
            "improvement_tips": [
                "At band 9, the response is complete; maintain the balanced structure in future essays.",
                "Consider mentioning the age of students briefly to add further nuance.",
            ],
        },
    },
    # ---------------- Q4: Working from home vs office (discussion) ----------------
    4: {
        "5": {
            "band": 5,
            "answer_text": (
                "Now many people work from home, and some people like it, but other people still want to "
                "work in an office. I think both have good and bad things.\n"
                "Working from home is good because people can save time and money. They do not travel "
                "every day, so they have more time with their family. For example, my father works from "
                "home and he has breakfast with us every day. Also, people can wear comfortable clothes.\n"
                "But working in an office is also good. People can talk with their colleagues and help "
                "each other. When they have a problem, they can ask a friend at work. Also, in the "
                "office, people can separate work and home, which is good for their mind.\n"
                "In my opinion, working from home is good for some people, but I think going to the "
                "office is better because I like to see my colleagues. It depends on the person.\n"
                "In conclusion, working from home and working in an office both have advantages, and the "
                "best choice depends on the person's job and life."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "Both views are presented with a personal opinion at the end, and some examples are "
                "included. However, the ideas are simple and the language is basic, with limited "
                "vocabulary and repetitive structures. The conclusion could be more decisive."
            ),
            "improvement_tips": [
                "Give each view a fully developed paragraph with a clear topic sentence.",
                "Use connectors such as 'however', 'in contrast' and 'for instance'.",
                "Replace simple words like 'good' and 'bad' with more precise alternatives.",
                "Make the opinion clearer in the introduction as well as the conclusion.",
                "Improve sentence variety and accuracy.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Remote working has grown rapidly in recent years, leading to a lively debate about "
                "whether people are better off at home or in the office. While both arrangements have "
                "merits, I believe that the ideal workplace depends on the individual and the nature of "
                "their work.\n"
                "There are compelling reasons to favour working from home. Perhaps the most obvious is "
                "the elimination of the daily commute, which saves considerable time and money and "
                "reduces stress. Remote workers often enjoy greater flexibility and can organise their "
                "day around family responsibilities. Moreover, without the distractions of an open-plan "
                "office, many people find they can concentrate more deeply and complete tasks more "
                "efficiently.\n"
                "On the other hand, the office offers benefits that are difficult to replicate at home. "
                "Face-to-face interaction with colleagues fosters collaboration and spontaneous problem "
                "solving, and many employees value the social side of work. The office also provides a "
                "clear boundary between professional and personal life, which can help people switch off "
                "at the end of the day. For younger employees in particular, being in the office can "
                "accelerate learning and career development.\n"
                "In my view, a hybrid approach is the most sensible compromise, allowing employees to "
                "benefit from both flexibility and collaboration. Whatever the choice, the key is to "
                "match the arrangement to the demands of the job and the preferences of the person.\n"
                "In conclusion, both remote work and office-based work have distinct advantages, and "
                "neither is inherently superior. The best solution is one that balances individual needs "
                "with the requirements of the team."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "Both views are discussed in a balanced, well-organised way, and a clear personal opinion "
                "is offered. Cohesion is effective and vocabulary is appropriate. The arguments are solid "
                "but could be supported with more specific examples and slightly more sophisticated "
                "language."
            ),
            "improvement_tips": [
                "Add a concrete example (e.g., a specific profession) to illustrate each view.",
                "Use more advanced vocabulary such as 'commute', 'work-life balance' and 'collaborative culture'.",
                "Vary the grammar with some complex structures.",
                "Strengthen the opinion by stating it more clearly in the conclusion.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The expansion of remote work has ignited a vigorous debate about the future of the "
                "office. Both arrangements, I believe, possess genuine merits, and the superiority of "
                "one over the other is largely contingent upon the nature of the role and the disposition "
                "of the individual.\n"
                "The virtues of working from home are considerable. Chief among them is the abolition of "
                "the commute, which bestows upon employees additional hours each day and a marked "
                "reduction in both expense and stress. Flexibility of this kind enables workers to "
                "reconcile professional obligations with family life, and many report that home provides "
                "a calmer environment for sustained, focused work, free from the interruptions endemic to "
                "shared offices. For roles that demand deep concentration, this can translate into "
                "measurably higher productivity.\n"
                "The office, however, retains an irreplaceable social and professional function. "
                "Colleagues who interact in person collaborate more readily, solving problems through "
                "spontaneous exchanges that videoconferencing cannot fully replicate. For new and junior "
                "employees, physical proximity to experienced colleagues accelerates learning, mentorship "
                "and career progression. Moreover, the office imposes a valuable structure upon the day, "
                "delineating work from leisure and thereby mitigating the risk of burnout that can afflict "
                "home workers.\n"
                "It seems to me, therefore, that the most enlightened employers will adopt a hybrid model, "
                "affording employees the flexibility of remote work while preserving the collaborative "
                "benefits of the office. Such an arrangement acknowledges that productivity is not a "
                "function of location but of the fit between task, environment and individual.\n"
                "In conclusion, neither working from home nor working in the office is universally "
                "superior; each confers advantages that are context-dependent. A considered hybrid approach "
                "offers the most promising path forward."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This is a sophisticated and fully developed discussion of both views, culminating in a "
                "clear personal position. The response is coherently organised with skilful use of "
                "cohesive devices. The lexical range is impressive and grammatical structures are "
                "complex and precise."
            ),
            "improvement_tips": [
                "No changes required at band 9; maintain the balance of depth across paragraphs.",
            ],
        },
    },
    # ---------------- Q5: Zoos (discussion) ----------------
    5: {
        "5": {
            "band": 5,
            "answer_text": (
                "Zoos are places where people can see wild animals. Some people think zoos are bad "
                "because animals are not free, but other people think zoos are important for protecting "
                "animals.\n"
                "In zoos, animals live in small places. They cannot run and fly like in the forest. For "
                "example, a tiger in the zoo stays in a small cage all day, and it looks sad. This is why "
                "some people say zoos are cruel. Also, some zoos are not clean and animals get sick.\n"
                "But zoos also help animals. Many animals are in danger, and zoos keep them safe and help "
                "them have babies. When animals have babies in the zoo, the number of animals can grow. "
                "Also, children can learn about animals by visiting zoos and seeing them with their own "
                "eyes.\n"
                "In my opinion, zoos are good if they are big and clean, but bad zoos should close. "
                "Animals should have enough space to move.\n"
                "In conclusion, zoos have both good and bad points. They should be improved so that "
                "animals are happy and people can still learn."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "Both sides of the argument are covered with a personal opinion and a relevant example. "
                "The structure is clear but the language is basic, with simple vocabulary and some "
                "grammatical errors. The response stays relevant throughout."
            ),
            "improvement_tips": [
                "Expand each paragraph with more detail and clearer topic sentences.",
                "Use a wider range of vocabulary: 'enclosures', 'endangered species', 'conservation'.",
                "Link paragraphs with connectors such as 'however' and 'in addition'.",
                "Check subject-verb agreement ('animals get sick', 'zoos are clean').",
                "Make the conclusion summarise both sides before giving your opinion.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The role of zoos in modern society is a contentious issue, with critics condemning them "
                "as prisons for animals and supporters praising them as centres of conservation. In my "
                "view, while poorly run zoos are indefensible, well-managed zoological gardens perform a "
                "valuable role in protecting species and educating the public.\n"
                "Opponents of zoos argue that confining wild animals is inherently cruel. In the wild, "
                "animals roam freely over large territories, whereas in many zoos they are restricted to "
                "small enclosures that bear little resemblance to their natural habitat. Such conditions "
                "can lead to physical and psychological distress, evident in repetitive behaviours often "
                "seen in captive animals. Critics also note that some zoos operate primarily for profit, "
                "with animal welfare a secondary concern.\n"
                "Supporters, however, point to the vital conservation work that accredited zoos carry "
                "out. Many endangered species have been saved from extinction through carefully managed "
                "breeding programmes, and zoos often fund research and habitat protection. Furthermore, "
                "for most people, particularly children, a zoo may be the only place they ever see a "
                "real tiger or elephant; this experience can inspire a lifelong interest in wildlife "
                "conservation.\n"
                "In conclusion, I believe that zoos are neither wholly good nor wholly bad. When animals "
                "are kept in spacious, naturalistic environments and the institution is devoted to "
                "conservation and education, zoos deserve our support. It is the poor quality of some "
                "zoos that is the real problem, not the idea of the zoo itself."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay addresses both views fairly and reaches a clear, nuanced position. Arguments "
                "are developed in well-structured paragraphs with effective cohesion. The vocabulary is "
                "accurate and appropriate, though it could be more sophisticated, and the examples are "
                "general rather than specific."
            ),
            "improvement_tips": [
                "Include a specific example of a successful breeding programme (e.g., pandas) to add weight.",
                "Use more precise terms such as 'enrichment', 'captive breeding' and 'ethical treatment'.",
                "Vary sentence structures, including some complex and conditional forms.",
                "Ensure the personal opinion is clearly signalled in the introduction.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "Few institutions provoke such polarised opinions as the zoo. For some, it is a window "
                "onto the natural world; for others, an emblem of human cruelty towards captive animals. "
                "I would contend that the legitimacy of zoos hinges entirely on their ethical standards "
                "and conservation credentials, rather than on the principle of keeping animals in "
                "captivity per se.\n"
                "The ethical case against zoos is not easily dismissed. Wild creatures possess an "
                "instinctive need for space, autonomy and the complex stimuli of their natural "
                "environments, none of which a conventional enclosure can adequately provide. The "
                "consequences of confinement are frequently visible: stereotypic behaviours, reduced "
                "lifespans and physiological stress. Where zoos are operated primarily as commercial "
                "spectacles, with little regard for welfare, such criticisms are entirely justified, and "
                "the case for closure is compelling.\n"
                "Conversely, the modern zoological garden has evolved into a serious instrument of "
                "conservation. Accredited institutions coordinate breeding programmes that have rescued "
                "numerous species from the brink of extinction, and they finance anti-poaching and "
                "habitat-restoration initiatives in the wild. Equally significant is their educational "
                "function: for many urban children, the zoo provides the only tangible encounter with "
                "species such as elephants or gorillas, and this exposure can foster the environmental "
                "consciousness that future conservation depends upon.\n"
                "On balance, I am persuaded that the value of a zoo should be judged not by the abstract "
                "question of whether animals belong in captivity, but by the quality of its care and its "
                "contribution to conservation. Zoos that meet these standards earn their place; those "
                "that do not should be closed.\n"
                "In conclusion, therefore, the debate is best resolved by regulation and accountability "
                "rather than by wholesale condemnation or defence of zoos."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay engages deeply with both perspectives and frames the issue with exceptional "
                "nuance, concluding that the ethical standing of zoos depends on their standards. The "
                "language is precise and sophisticated, cohesion is seamless, and the grammatical range "
                "is extensive and accurate."
            ),
            "improvement_tips": [
                "No improvement needed; this response is at the highest level.",
            ],
        },
    },
    # ---------------- Q6: Children doing housework (discussion) ----------------
    6: {
        "5": {
            "band": 5,
            "answer_text": (
                "Some parents want their children to help with housework, but other parents think "
                "children should only study. I think children should help a little at home.\n"
                "When children do housework, they learn important things. They learn to clean, cook and "
                "take care of their things. For example, my mother taught me to cook rice when I was "
                "ten, and now I can cook for myself. Also, children who help at home understand their "
                "parents better because they see how much work is needed.\n"
                "But children also need time for homework. If they do too much housework, they can be "
                "tired and get bad marks at school. Studies are important for their future, so parents "
                "should not give children too many jobs.\n"
                "I think children should do small jobs like cleaning their room and washing dishes, but "
                "studying must come first.\n"
                "In conclusion, children should help with housework, but not too much, because they also "
                "need to study and play."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "Both views are presented with a clear personal opinion. The response is relevant and "
                "includes a personal example, but the language is simple and the paragraphs are short. "
                "There is some repetition and basic grammatical structure."
            ),
            "improvement_tips": [
                "Develop both views in fuller paragraphs.",
                "Use more precise vocabulary such as 'responsibilities', 'chores' and 'academic workload'.",
                "Add linking phrases to show contrast, e.g., 'in contrast', 'nevertheless'.",
                "Use conditional sentences to express balanced ideas.",
                "Strengthen the conclusion by summarising your main reasons.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Whether children should contribute to household chores is a question on which parents "
                "differ considerably. While some view housework as an essential lesson in responsibility, "
                "others insist that children's time is better spent on their studies. I believe a balanced "
                "allocation of both is the most sensible approach.\n"
                "Those who favour children doing housework argue that it builds character. Tasks such as "
                "cleaning, cooking and tidying teach practical life skills and instil a sense of "
                "responsibility from an early age. Children who help at home also develop an appreciation "
                "for the effort involved in running a household and are often more independent and "
                "self-reliant as a result. In many cultures, contributing to family life is simply "
                "regarded as a normal part of growing up.\n"
                "The opposing view holds that childhood should be devoted to education. Academic success "
                "increasingly depends on study time, and parents who burden their children with chores "
                "may fear this hampers their progress. There is also the argument that children need time "
                "to play, rest and pursue hobbies, all of which are important for healthy development. "
                "Overloading children with housework could leave them stressed and exhausted.\n"
                "In my view, the solution lies in moderation. Children should certainly help with "
                "age-appropriate tasks, but this should not come at the expense of their education or "
                "leisure. Such a balance teaches responsibility while preserving time for learning and "
                "play.\n"
                "In conclusion, both perspectives have merit, and the most reasonable position is to "
                "involve children in housework without allowing it to dominate their lives."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay discusses both views fairly, develops each in a clear paragraph, and offers a "
                "balanced personal opinion. The vocabulary is appropriate and cohesion is handled well. "
                "The arguments are solid though examples remain general."
            ),
            "improvement_tips": [
                "Add a concrete example, such as a comparison between two families, to illustrate the argument.",
                "Use more advanced vocabulary: 'responsibility', 'self-discipline', 'well-rounded'.",
                "Vary sentence beginnings to improve readability.",
                "Make the conclusion more decisive about the exact balance recommended.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The extent to which children should participate in household chores remains a point of "
                "disagreement among parents, with opinions divided between those who regard such duties "
                "as formative and those who believe academic pursuits should take precedence. On balance, "
                "I am inclined to believe that a measured involvement in household tasks is highly "
                "beneficial, provided it does not encroach upon a child's education or wellbeing.\n"
                "There are compelling reasons to regard housework as a valuable part of childhood. "
                "Practical chores such as cooking, cleaning and budgeting cultivate competencies that no "
                "classroom can fully teach, equipping young people with the self-sufficiency they will "
                "require in adulthood. Equally important is the moral dimension: children who contribute "
                "to the running of the household develop empathy, gratitude and a sense of shared "
                "responsibility, qualities that predict success in relationships and the workplace. "
                "Research in developmental psychology consistently links early responsibility with "
                "greater resilience and independence in later life.\n"
                "The contrary view, however, deserves serious consideration. In an era of intense "
                "academic competition, time spent on chores can seem like time stolen from study, and "
                "anxious parents may reasonably wish to shield their children from such burdens. "
                "Moreover, excessive demands can produce stress and resentment, undermining the very "
                "lessons in cooperation that housework is meant to teach. The danger lies not in asking "
                "children to help, but in expecting them to carry a disproportionate load.\n"
                "It follows that the optimal approach is proportionality: chores should be "
                "age-appropriate, clearly defined and balanced against schoolwork and leisure. A child "
                "who helps with a few daily tasks learns responsibility without sacrificing the time "
                "needed to grow, learn and play.\n"
                "In conclusion, while both perspectives contain elements of truth, I maintain that "
                "moderate participation in household chores benefits children immensely, so long as it "
                "remains in harmony with their education and their need for rest."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This is a fully developed, nuanced discussion of both views, synthesised into a clear, "
                "balanced position. The arguments are supported with reference to developmental research, "
                "cohesion is seamless, and the language is sophisticated and precise throughout."
            ),
            "improvement_tips": [
                "No significant improvement required at this level.",
            ],
        },
    },
    # ---------------- Q7: Advertising (discussion) ----------------
    7: {
        "5": {
            "band": 5,
            "answer_text": (
                "Advertising is everywhere. We see it on television, on the internet and on the street. "
                "Some people say advertising helps us buy things, but other people say it makes us buy "
                "things we do not need.\n"
                "Advertising helps us in some ways. When we see an advertisement for a new phone, we can "
                "know about it and compare it with other phones. Also, advertisements tell us about "
                "cheap offers and sales, so we can save money. For example, my family found a good "
                "washing machine because we saw it in an advertisement.\n"
                "But advertising also has problems. Many advertisements make things look better than "
                "they are, and people buy them and feel sad later. For example, food advertisements make "
                "children want unhealthy food. Also, some people spend too much money because they see "
                "advertisements and want to buy everything.\n"
                "In my opinion, advertising is good if we are careful, but it can be bad if we trust "
                "everything we see.\n"
                "In conclusion, advertising helps people make choices, but it can also make them buy "
                "unnecessary things."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "Both views are presented with relevant examples and a personal opinion. The response is "
                "coherent but uses simple language with limited range. The structure is acceptable, and "
                "the conclusion restates the position."
            ),
            "improvement_tips": [
                "Use more formal language instead of conversational expressions.",
                "Develop paragraphs with clearer topic sentences and more support.",
                "Use vocabulary such as 'persuasion', 'consumer', 'misleading'.",
                "Add more sophisticated linking devices.",
                "Check for grammatical accuracy, especially verb tenses.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Advertising has become an unavoidable feature of modern life, and its influence on "
                "consumer behaviour is hotly debated. While advertising can certainly inform and guide "
                "consumers, I believe it also encourages impulsive and unnecessary spending, making its "
                "overall effect questionable.\n"
                "On the positive side, advertising serves an important informational function. Through "
                "advertisements, consumers learn about new products and services, compare prices and "
                "discover special offers that they might otherwise miss. This is particularly useful "
                "for products such as cars or electronics, where informed choices can result in "
                "considerable savings. Moreover, advertising funds many free services, including "
                "websites and television channels, which the public would otherwise have to pay for.\n"
                "On the negative side, advertising is frequently designed to manipulate rather than "
                "inform. Marketers employ psychological techniques to create desire, often presenting "
                "products in an unrealistically attractive light. Children are especially vulnerable, "
                "and advertising can encourage them to demand junk food and expensive toys. At a "
                "societal level, constant exposure to advertising can foster materialism and consumer "
                "debt, as people are persuaded to buy things they neither need nor can afford.\n"
                "In my opinion, advertising is a double-edged sword. It can be a helpful source of "
                "information, but it requires a critical and educated consumer to use it well. "
                "Stricter regulation, particularly regarding advertisements aimed at children, would "
                "help mitigate its negative effects.\n"
                "In conclusion, advertising has both benefits and drawbacks. Its value depends largely "
                "on how consumers engage with it and how effectively it is regulated."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay discusses both views in a balanced manner, presents clear arguments, and offers "
                "a personal opinion with a practical suggestion. Cohesion is effective, and the vocabulary "
                "is accurate and reasonably varied, though a wider range would strengthen it further."
            ),
            "improvement_tips": [
                "Include a specific, credible example of misleading advertising.",
                "Use more sophisticated vocabulary such as 'manipulative', 'consumerism' and 'ethical regulation'.",
                "Vary complex sentence structures to add sophistication.",
                "Tighten the conclusion so it flows more forcefully.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "In an age saturated by commercial messages, the role of advertising in shaping consumer "
                "behaviour invites vigorous debate. Although advertising undeniably equips consumers with "
                "valuable information, I would argue that its persuasive, often manipulative character "
                "frequently impels people to purchase goods they neither require nor truly desire.\n"
                "The informational value of advertising should not be underestimated. It functions as a "
                "vital conduit between producers and consumers, alerting the public to new products, "
                "comparative prices and promotional offers. For high-involvement purchases such as "
                "automobiles or electronic equipment, well-crafted advertising can facilitate informed "
                "decision-making and yield significant savings. It also underpins the economic model of "
                "many free platforms, from search engines to streaming services, effectively subsidising "
                "content that consumers enjoy at no cost.\n"
                "Yet the darker face of advertising lies in its capacity to manufacture desire rather "
                "than satisfy genuine need. Sophisticated psychological profiling and the exploitation of "
                "emotional vulnerabilities mean that advertising frequently manipulates rather than "
                "informs, creating a culture of insatiable consumption. The vulnerability of children, "
                "who lack the cognitive tools to discern persuasive intent, is particularly troubling, "
                "and the proliferation of targeted advertising has been implicated in rising consumer "
                "debt and materialism across many societies.\n"
                "On balance, I am persuaded that advertising is neither inherently beneficial nor "
                "inherently harmful; its effects hinge upon the ethics of practitioners and the "
                "discernment of audiences. Robust regulation, particularly of marketing directed at "
                "minors, coupled with media literacy education, offers the most promising means of "
                "harnessing advertising's benefits while curbing its excesses.\n"
                "In conclusion, although advertising can inform and empower consumers, its propensity to "
                "manipulate renders its overall influence on our purchasing habits decidedly "
                "double-edged. Its value, ultimately, depends on the vigilance of those who encounter it."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay offers a nuanced, fully developed discussion of both sides, concluding with a "
                "measured personal position. Arguments are sophisticated and well supported, cohesion is "
                "seamless, and the lexical and grammatical range is extensive and precise."
            ),
            "improvement_tips": [
                "This is a band 9 response; no changes are required.",
            ],
        },
    },
    # ---------------- Q8: Living in a big city (advantages/disadvantages) ----------------
    8: {
        "5": {
            "band": 5,
            "answer_text": (
                "Many people are moving from villages to big cities. Living in a big city has good and "
                "bad things.\n"
                "There are many advantages. In a big city, people can find good jobs more easily. For "
                "example, my uncle moved to the city and found a job in a company very quickly. Also, "
                "cities have good hospitals and schools. People can go to the cinema, restaurants and "
                "parks. There are many things to do in a city.\n"
                "But there are also disadvantages. Life in the city is expensive. Houses are very "
                "expensive, and food costs more money. Also, cities are noisy and there is a lot of "
                "traffic. People sometimes feel stressed because the city is busy all the time. My aunt "
                "says she misses the quiet village.\n"
                "In my opinion, living in a big city is good for young people because there are more "
                "opportunities, but it is not good for old people who want peace.\n"
                "In conclusion, big cities give people jobs and fun, but life there is costly and busy. "
                "It depends on what people want."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response addresses both advantages and disadvantages with relevant examples. The "
                "language is simple with basic vocabulary, and the paragraphs are short but clearly "
                "organised. The opinion is present but the conclusion could be stronger."
            ),
            "improvement_tips": [
                "Expand each paragraph with more supporting detail and examples.",
                "Use richer vocabulary such as 'opportunities', 'cost of living', 'amenities'.",
                "Add linking phrases like 'on the one hand' and 'on the other hand'.",
                "Improve sentence variety and grammatical accuracy.",
                "Make the conclusion more decisive.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The continuing migration of people from rural areas to large cities is a defining feature "
                "of the modern world. While urban living offers considerable benefits, it also brings "
                "significant drawbacks, and the balance of these depends on individual circumstances.\n"
                "The advantages of city life are well documented. Cities are economic hubs that offer a "
                "far wider range of employment opportunities than the countryside, which is why so many "
                "young people relocate there in search of careers. They also provide superior amenities: "
                "world-class hospitals, universities, cultural institutions and entertainment options are "
                "all concentrated in urban areas. The sheer variety of people and experiences in a city "
                "can also broaden one's horizons and encourage personal growth.\n"
                "However, urban living has its downsides. The cost of living, particularly housing, is "
                "often prohibitively high, and many city dwellers struggle to save money or own property. "
                "Cities are also associated with overcrowding, heavy traffic and air pollution, all of "
                "which can harm quality of life. The relentless pace of city life can contribute to "
                "stress and a sense of isolation, even amid millions of neighbours.\n"
                "In my view, whether city life is advantageous depends largely on a person's stage of "
                "life and priorities. Young professionals may thrive on the opportunities a city offers, "
                "whereas those seeking peace and affordable living may be happier in smaller towns.\n"
                "In conclusion, living in a big city brings both significant opportunities and notable "
                "challenges. It is not universally better or worse, but simply a different way of life "
                "with its own costs and rewards."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay clearly addresses both advantages and disadvantages and concludes with a "
                "nuanced position. Paragraphs are well developed and cohesive, and the vocabulary is "
                "appropriate. The response is strong, though it relies on general points rather than "
                "specific examples."
            ),
            "improvement_tips": [
                "Add a specific example, such as a named city or a personal case study.",
                "Use more advanced vocabulary such as 'urban sprawl', 'cost of living' and 'amenities'.",
                "Include a wider range of complex grammatical structures.",
                "Strengthen the conclusion with a memorable final sentence.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The exodus from countryside to metropolis has accelerated dramatically in recent "
                "decades, transforming the demographic landscape of nations worldwide. Urban life confers "
                "undoubted benefits, yet it is accompanied by costs that are equally real, and a fair "
                "assessment must weigh both with care.\n"
                "The attractions of the city are manifold. Economically, cities are engines of "
                "opportunity, concentrating industries, enterprises and employment across every sector, "
                "making them magnets for the ambitious and the talented. This economic vitality is "
                "matched by unrivalled access to services: leading medical facilities, prestigious "
                "universities, and a rich cultural life of theatres, galleries and festivals. The "
                "density of human interaction also fosters innovation and cosmopolitanism, exposing "
                "residents to diverse ideas and perspectives that broaden the mind.\n"
                "Against these advantages must be set formidable drawbacks. Housing in major cities has "
                "become exorbitantly expensive, pushing many into cramped accommodation or distant "
                "suburbs with punishing commutes. Congestion and pollution degrade the urban environment, "
                "with particulate matter in some megacities posing serious health risks. Psychologically, "
                "the anonymity and pace of city life can engender loneliness and chronic stress, "
                "paradoxically leaving individuals more isolated despite living amid millions.\n"
                "Whether these balances favour the city is, I believe, profoundly personal. For the young "
                "and career-driven, the opportunities and stimulation of urban life are likely to "
                "outweigh its strains; for families seeking space, tranquillity and affordability, the "
                "countryside may prove the wiser choice.\n"
                "In conclusion, big-city living offers exceptional opportunities for prosperity and "
                "culture, but exacts a price in cost, congestion and stress. The decision to embrace it, "
                "therefore, is less about which option is objectively superior and more about what each "
                "individual values most."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay addresses the question comprehensively, presenting well-developed advantages "
                "and disadvantages before reaching a balanced, personal conclusion. The language is "
                "sophisticated and precise, cohesion is seamless, and complex grammatical structures are "
                "used accurately throughout."
            ),
            "improvement_tips": [
                "No improvement needed; this is a band 9 response.",
            ],
        },
    },
    # ---------------- Q9: Public transport vs cars (advantages/disadvantages) ----------------
    9: {
        "5": {
            "band": 5,
            "answer_text": (
                "Many governments now want people to use public transport like buses and trains instead "
                "of their cars. Using public transport has good and bad things.\n"
                "There are many good things. Public transport is cheaper than using a car, because we "
                "do not buy petrol. For example, a bus ticket is much cheaper than a full tank of "
                "petrol. Also, public transport is better for the environment because one bus can carry "
                "many people, so there is less pollution. People can also relax and read on the bus "
                "instead of driving.\n"
                "But there are also bad things. Public transport is not always on time, and people have "
                "to wait a long time. It can also be crowded, especially in the morning. In some places, "
                "there is no bus or train, so people have no choice but to use their car.\n"
                "In my opinion, public transport is good for cities, but governments must make it better "
                "so that people will use it.\n"
                "In conclusion, public transport is cheaper and cleaner, but it is not always convenient. "
                "Governments should improve it to make people happy."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "Both advantages and disadvantages are listed with clear examples. The structure is "
                "logical but the language is simple, with basic vocabulary and repetitive phrasing. The "
                "conclusion offers a sensible suggestion."
            ),
            "improvement_tips": [
                "Write longer, better-developed paragraphs.",
                "Use more specific vocabulary: 'congestion', 'emissions', 'reliability'.",
                "Vary sentence openings and use more connectors.",
                "Improve grammatical range, including modal verbs and conditionals.",
                "Add a stronger personal opinion with reasons.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "With traffic and pollution worsening in cities around the world, governments are "
                "increasingly urging citizens to switch from private cars to public transport. While "
                "such a shift offers clear benefits, public transport is not without its drawbacks, and a "
                "balanced assessment is necessary.\n"
                "The advantages of public transport are considerable. Financially, buses and trains are "
                "usually far cheaper than running a car, which involves fuel, insurance and maintenance "
                "costs. Environmentally, they are far more efficient: a single full bus removes dozens of "
                "cars from the road, substantially reducing emissions and congestion. Commuters can also "
                "use their journey productively, reading, working or simply relaxing, rather than "
                "enduring the stress of driving.\n"
                "The disadvantages, however, are equally significant. Public transport can be "
                "unreliable, with delays and cancellations disrupting people's plans. It is often "
                "crowded and uncomfortable during rush hours, and in many areas services are "
                "infrequent or non-existent, especially in the suburbs and countryside. For those with "
                "young children or heavy luggage, the convenience of a car is difficult to replace.\n"
                "In my view, public transport is an excellent option in dense urban areas where it is "
                "frequent and reliable. The key to encouraging its use is investment: if governments "
                "make services punctual, affordable and comfortable, far more people will choose them "
                "over their cars.\n"
                "In conclusion, public transport offers clear financial and environmental advantages, "
                "but its success depends on quality and coverage. With the right investment, it can "
                "become a genuinely attractive alternative to the private car."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay presents balanced advantages and disadvantages with a clear, reasoned "
                "conclusion. Paragraphs are well organised and cohesive, and the vocabulary is "
                "appropriate. The arguments are convincing though based on general points."
            ),
            "improvement_tips": [
                "Add a concrete example of a city where good public transport succeeded.",
                "Use more sophisticated vocabulary such as 'infrastructure', 'frequency' and 'viable alternative'.",
                "Include more varied complex sentence structures.",
                "Tighten the introduction to state your position more directly.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "As urban congestion and environmental degradation intensify, policymakers have made the "
                "promotion of public transport a cornerstone of modern city planning. The case for such a "
                "shift is compelling, yet a dispassionate analysis reveals that its success is contingent "
                "upon the quality of the service provided.\n"
                "The benefits of bus and rail networks are numerous and well substantiated. Economically, "
                "they offer a far more affordable means of travel than car ownership, sparing commuters "
                "the cumulative burden of fuel, insurance, parking and depreciation. Environmentally, the "
                "superiority of mass transit is beyond dispute: a single articulated bus can carry as many "
                "passengers as forty private cars, yielding dramatic reductions in emissions and traffic "
                "density. For the individual, there is also the reclaiming of time and the relief from "
                "driving fatigue that only a seat on a train can provide.\n"
                "Yet the weaknesses of public transport are inseparable from its strengths. Reliability "
                "remains its Achilles' heel: delays, breakdowns and industrial action can undermine the "
                "punctuality upon which commuters depend. Overcrowding during peak hours erodes comfort "
                "and dignity, and the scarcity of services in peripheral areas forces many residents into "
                "car ownership by necessity rather than choice. Moreover, for families with small "
                "children, the flexibility and door-to-door convenience of the car are difficult to "
                "surpass.\n"
                "I would therefore contend that the merits of public transport are contingent upon "
                "investment and governance. Where networks are frequent, affordable and well-integrated, "
                "as in several European cities, they flourish and are widely embraced; where they are "
                "neglected, they remain a poor alternative. The solution is not simply to extol the "
                "virtues of public transport but to make it genuinely superior.\n"
                "In conclusion, public transport offers clear economic and environmental advantages over "
                "private cars, but these advantages are realised only when the service is dependable, "
                "extensive and comfortable. Under the right conditions, it is unquestionably the more "
                "sensible choice."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay provides a sophisticated and balanced treatment of the topic, with a nuanced "
                "conclusion that ties the benefits to the quality of provision. The vocabulary is "
                "precise and varied, cohesion is impeccable, and the grammatical range is extensive and "
                "accurate."
            ),
            "improvement_tips": [
                "No improvement required at this level.",
            ],
        },
    },
    # ---------------- Q10: Studying abroad (advantages/disadvantages) ----------------
    10: {
        "5": {
            "band": 5,
            "answer_text": (
                "More and more students are going to study in other countries. Studying abroad has good "
                "and bad things.\n"
                "There are many advantages. Students can learn a new language very fast because they "
                "hear it every day. For example, my friend studied in the UK and now she speaks English "
                "very well. Also, students can see new places and make friends from all over the world. "
                "They become more independent because they do everything by themselves.\n"
                "But there are also disadvantages. Studying abroad is very expensive. Students must pay "
                "for the university and for their home and food. Some students feel lonely and miss "
                "their family. Also, it can be difficult to understand the new culture and food at the "
                "beginning.\n"
                "In my opinion, studying abroad is a great chance, but students should be ready for "
                "difficulties.\n"
                "In conclusion, studying abroad helps students learn a language and become independent, "
                "but it is expensive and can be lonely."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response covers both advantages and disadvantages with relevant personal examples. "
                "The structure is clear and the language is simple but understandable. Some sentences are "
                "repetitive and the vocabulary range is limited."
            ),
            "improvement_tips": [
                "Use a wider range of vocabulary: 'cultural immersion', 'tuition fees', 'homesickness'.",
                "Develop paragraphs with more supporting detail.",
                "Use more linking words such as 'in addition', 'however', 'consequently'.",
                "Check verb tense consistency.",
                "Make the conclusion more detailed.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The number of students pursuing higher education in foreign countries has risen sharply "
                "in recent years. While studying abroad offers transformative opportunities, it also "
                "presents significant challenges, and its value depends greatly on the individual "
                "student's situation.\n"
                "The advantages of studying abroad are considerable. Perhaps the most obvious is the "
                "opportunity for cultural immersion, which accelerates language acquisition far more "
                "effectively than classroom study alone. Living in another country also fosters "
                "independence and adaptability, as students must manage finances, accommodation and "
                "daily life without their usual support networks. Moreover, an international degree can "
                "significantly enhance a graduate's employability, as employers increasingly value "
                "cross-cultural experience.\n"
                "The drawbacks, however, should not be overlooked. Cost is the most significant: "
                "international tuition fees and living expenses are prohibitively high for many "
                "families, and exchange-rate fluctuations can worsen the burden. Students also commonly "
                "experience homesickness and cultural adjustment difficulties, which can affect their "
                "academic performance and mental health. Without adequate support, some struggle to "
                "adapt and fail to realise the benefits of the experience.\n"
                "In my view, studying abroad is a rewarding investment for students who are "
                "sufficiently prepared and supported. The key is to weigh the personal and financial "
                "costs realistically against the long-term benefits of a global education.\n"
                "In conclusion, while studying abroad offers outstanding opportunities for personal and "
                "academic growth, it is not without its challenges. For well-prepared students with "
                "adequate support, the benefits far outweigh the difficulties."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay gives a balanced account of advantages and disadvantages with a clear final "
                "position. The response is well organised and cohesive, and the vocabulary is "
                "appropriate. It could be improved with more specific examples and slightly more "
                "sophisticated expression."
            ),
            "improvement_tips": [
                "Add a specific example, such as a particular country or field of study.",
                "Use more advanced vocabulary: 'employability', 'socio-economic barriers', 'intercultural competence'.",
                "Vary sentence structures, including passive and conditional forms.",
                "Make the introduction more compelling.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The dramatic growth in international student mobility has made studying abroad one of "
                "the defining educational phenomena of our time. While the experience offers "
                "unmistakable benefits, it entails equally tangible costs, and a judicious evaluation "
                "must take account of both.\n"
                "The advantages of an overseas education are profound and multifaceted. Chief among them "
                "is total linguistic and cultural immersion, which produces fluency and cultural "
                "competence in a manner that classroom instruction can seldom match. Away from home, "
                "students are compelled to navigate unfamiliar systems, manage limited budgets and build "
                "new social networks, developing a resilience and self-reliance that proves invaluable "
                "throughout life. Professionally, an international qualification is increasingly "
                "regarded as a marker of ambition and adaptability, opening doors in a globalised "
                "labour market where cross-cultural experience is prized.\n"
                "The disadvantages are, however, substantial and often underestimated. Financially, "
                "studying abroad imposes a heavy burden, encompassing tuition, accommodation and travel, "
                "which may saddle families with years of debt. Psychologically, the experience can be "
                "isolating: students far from home may suffer acute homesickness, language barriers and "
                "culture shock, all of which can impair both wellbeing and academic performance. In some "
                "cases, these pressures culminate in students abandoning their studies altogether, "
                "having gained little beyond considerable expense.\n"
                "I would suggest, therefore, that the wisdom of studying abroad lies less in the decision "
                "itself than in the preparation and support surrounding it. Students who embark with "
                "realistic expectations, adequate funding and strong institutional support are likely to "
                "reap enormous rewards; those without such foundations may find the costs dominate.\n"
                "In conclusion, studying abroad offers exceptional opportunities for growth, learning "
                "and career advancement, but it demands significant financial and emotional investment. "
                "Where preparation and support are strong, the benefits clearly outweigh the "
                "difficulties."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response offers a comprehensive, nuanced evaluation of studying abroad, balancing "
                "rich advantages against real costs and reaching a carefully qualified conclusion. The "
                "language is sophisticated and precise, cohesion is seamless, and grammatical control is "
                "consistently accurate."
            ),
            "improvement_tips": [
                "No changes needed at this level.",
            ],
        },
    },
    # ---------------- Q11: Social media for news (advantages/disadvantages) ----------------
    11: {
        "5": {
            "band": 5,
            "answer_text": (
                "Now many people get their news from social media like Facebook and Twitter. Getting "
                "news from social media has good and bad things.\n"
                "The good thing is that news is very fast. When something happens, we can know about it "
                "in a few minutes on social media. Also, it is free. We do not pay money to read the "
                "news on the internet. For example, my brother learns about football news every day from "
                "social media.\n"
                "But there are also bad things. Some news on social media is not true. People write "
                "false things, and other people believe them. For example, last year there was false "
                "news about a famous singer, and many people believed it. Also, social media news is "
                "sometimes not complete, so people do not know the whole story.\n"
                "In my opinion, people should be careful with news from social media and check with "
                "other sources.\n"
                "In conclusion, social media gives us fast and free news, but it can be false, so we "
                "must be careful."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response clearly presents both advantages and disadvantages with relevant examples. "
                "The language is simple and occasionally informal, and the paragraphs could be more "
                "developed. The overall structure is logical."
            ),
            "improvement_tips": [
                "Use more formal vocabulary: 'misinformation', 'credibility', 'real-time'.",
                "Develop each paragraph with more detail.",
                "Improve grammar, particularly tense usage.",
                "Add more sophisticated connectors.",
                "Strengthen the conclusion with a clear final judgement.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Social media platforms have become a primary source of news for millions of people, "
                "gradually replacing traditional newspapers and television bulletins. This development "
                "brings both significant advantages and notable drawbacks.\n"
                "On the positive side, social media offers immediacy and accessibility that traditional "
                "media cannot match. Breaking news often appears on platforms within minutes, and users "
                "can follow developments in real time. The cost is also an advantage: access is free for "
                "the vast majority of users, democratising information in a way that newspapers could "
                "not. Furthermore, social media allows readers to engage directly with stories, comment "
                "on them and share diverse viewpoints.\n"
                "The negative aspects are equally serious. The most pressing is the proliferation of "
                "misinformation and fake news. Because anyone can publish without editorial oversight, "
                "false or misleading content can spread rapidly, reaching millions before it is "
                "corrected. Algorithms also tend to show users content that confirms their existing "
                "beliefs, creating echo chambers that polarise public opinion. Additionally, the brevity "
                "of posts can oversimplify complex issues, leaving readers poorly informed.\n"
                "In my view, social media is a valuable complement to traditional news sources, but it "
                "should not replace them. Users need to verify information from multiple sources and "
                "approach sensational content with caution.\n"
                "In conclusion, while social media makes news faster, cheaper and more engaging, its "
                "reliability is a serious concern. A critical, informed approach is essential for anyone "
                "who relies on it."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay addresses both advantages and disadvantages coherently, concluding with a "
                "sensible personal recommendation. The vocabulary is accurate and appropriate, and the "
                "paragraphs are well structured. It could be strengthened with specific, credible "
                "examples."
            ),
            "improvement_tips": [
                "Include a specific example of a misinformation case that had real consequences.",
                "Use more sophisticated vocabulary such as 'editorial oversight', 'echo chambers' and 'verification'.",
                "Vary complex sentence structures to add sophistication.",
                "Refine the introduction to be more compelling.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The ascendancy of social media as a primary news source has fundamentally altered the "
                "manner in which society consumes information, supplanting traditional journalistic "
                "outlets in the habits of millions. This transformation offers striking advantages, yet "
                "it is shadowed by equally profound risks that merit careful examination.\n"
                "The benefits are readily apparent. Social media provides unprecedented immediacy, "
                "delivering breaking developments to users within moments, and its global reach "
                "transcends the geographic constraints of traditional media. Its accessibility and "
                "absence of cost democratise information, enabling voices from every corner of society "
                "to participate in public discourse. Moreover, interactive features allow readers to "
                "scrutinise stories, debate interpretations and supply context in ways that passive "
                "consumption of a newspaper could never permit.\n"
                "The liabilities, however, are grave. The evaporation of editorial gatekeeping has "
                "spawned an epidemic of misinformation, in which fabricated content propagates with "
                "alarming velocity, often outpacing correction. Compounding this is the design of "
                "algorithms, which prioritise engagement and thereby confine users within echo chambers, "
                "reinforcing biases and fragmenting the public sphere. The compression of complex "
                "matters into fleeting posts further undermines the depth of understanding necessary "
                "for an informed citizenry, as nuance is sacrificed for virality.\n"
                "On balance, I would argue that social media has revolutionised the distribution of "
                "news for the better, but its unregulated character renders it a dangerous sole source "
                "of information. The remedy lies in media literacy and responsible consumption: users "
                "must triangulate sources, question provenance and resist the emotional pull of "
                "sensationalism.\n"
                "In conclusion, social media offers an immediacy and inclusivity that traditional media "
                "cannot rival, yet its vulnerability to misinformation is profound. Its worth as a news "
                "source is ultimately determined not by the platform itself, but by the discernment of "
                "those who use it."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This is a sophisticated, fully developed analysis of both sides, culminating in a "
                "nuanced personal position. The arguments are precise and well supported, cohesion is "
                "flawless, and the lexical and grammatical range is extensive and accurate."
            ),
            "improvement_tips": [
                "No improvement required at this band.",
            ],
        },
    },
    # ---------------- Q12: Traffic congestion (problem/solution) ----------------
    12: {
        "5": {
            "band": 5,
            "answer_text": (
                "Traffic is a big problem in many cities now. There are many cars on the road, and "
                "people spend a lot of time waiting. This problem has causes and solutions.\n"
                "One cause is that there are too many cars. The population is growing, and more people "
                "buy cars. In my city, every family has a car, and some have two cars. Another cause is "
                "that the roads are not wide enough. Old cities have small roads, but there are many "
                "new cars.\n"
                "There are solutions for this problem. Governments can build more roads and bridges. "
                "They can also make public transport better, like buses and trains, so people will not "
                "use their cars. For example, in Japan, many people use the train, and there is less "
                "traffic. Also, governments can ask people to use bicycles.\n"
                "In conclusion, traffic congestion happens because of too many cars and small roads. "
                "Governments should improve public transport and build more roads to solve this "
                "problem."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response identifies causes and proposes solutions with a relevant example. The "
                "structure is logical and the language is simple but functional. Vocabulary is basic "
                "and there is limited grammatical range."
            ),
            "improvement_tips": [
                "Use more precise vocabulary: 'congestion', 'infrastructure', 'urban planning'.",
                "Develop each idea in a fuller paragraph.",
                "Add more linking devices between ideas.",
                "Improve grammatical accuracy and variety.",
                "Conclude by linking the solutions directly to the causes.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Traffic congestion has become one of the most persistent problems facing modern cities, "
                "wasting time, increasing pollution and damaging productivity. This essay will examine "
                "the main causes of congestion and suggest practical solutions.\n"
                "The principal cause of traffic jams is the sheer volume of private vehicles on the "
                "roads. As cities grow and incomes rise, car ownership has increased dramatically, "
                "while road capacity has often remained static. Poor urban planning exacerbates the "
                "problem: many cities were designed around the car, with insufficient alternatives, and "
                "new residential areas are frequently built far from workplaces, making commuting by car "
                "almost unavoidable.\n"
                "There are several effective solutions. Governments could invest heavily in reliable, "
                "affordable public transport, including buses, trains and metro systems, giving "
                "commuters a genuine alternative to driving. The introduction of congestion charging, "
                "as seen in cities such as London and Singapore, has also proved successful in "
                "discouraging unnecessary car journeys. In addition, promoting cycling and "
                "walking through dedicated lanes and safer infrastructure can reduce short trips "
                "that currently clog city streets.\n"
                "In my view, a combination of these measures is essential, since no single solution "
                "will solve the problem on its own. Investment in public transport must be matched by "
                "policies that discourage car use and encourage more sustainable modes of travel.\n"
                "In conclusion, traffic congestion stems largely from excessive car use and poor "
                "planning. By improving public transport, implementing charging schemes and encouraging "
                "active travel, cities can significantly reduce this growing problem."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay clearly identifies causes and proposes a range of relevant, realistic "
                "solutions, supported by reference to successful examples. It is well organised and "
                "cohesive, with appropriate vocabulary. It could be strengthened with more specific "
                "statistics or details."
            ),
            "improvement_tips": [
                "Add concrete statistics or a more detailed example to support the argument.",
                "Use more sophisticated vocabulary such as 'urban sprawl', 'congestion charging' and 'modal shift'.",
                "Vary sentence structures to improve sophistication.",
                "Tighten the introduction to make the essay's scope explicit.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "Traffic congestion has emerged as one of the most intractable afflictions of the "
                "contemporary city, consuming hours of commuters' lives, degrading air quality and "
                "imposing a heavy toll on economic productivity. Addressing it demands an accurate "
                "diagnosis of its causes and the deployment of a coordinated set of solutions.\n"
                "The root of the problem lies primarily in the unchecked growth of private car "
                "ownership, itself a by-product of rising prosperity and urban expansion. As cities "
                "have spread outwards, employment and residential zones have become separated, "
                "rendering car travel for many a matter of necessity rather than choice. This growth "
                "in demand has been met, in most cities, by only marginal increases in road capacity, "
                "creating a chronic imbalance between the number of vehicles and the infrastructure "
                "designed to accommodate them. Compounding matters, fragmented governance and "
                "short-term planning have frequently prioritised road building over integrated "
                "transport strategies.\n"
                "The remedies, however, are well within reach if pursued with resolve. Foremost is the "
                "creation of a genuinely attractive public transport network: frequent, affordable and "
                "interconnected services that can absorb the journeys currently made by car. "
                "Congestion charging, successfully implemented in London and Singapore, provides a "
                "market-based incentive to ration road space, and the revenues it generates can be "
                "ring-fenced for transport investment. In parallel, redesigning streets to favour "
                "pedestrians and cyclists not only reduces traffic but improves public health, while "
                "mixed-use urban planning that reunites housing with workplaces diminishes the need to "
                "travel at all.\n"
                "I would therefore contend that the solution is not a single silver bullet but an "
                "integrated strategy, combining public investment, fiscal incentives and urban "
                "redesign. Only through such a holistic approach can cities hope to reclaim their "
                "streets and their citizens' time.\n"
                "In conclusion, congestion is the product of excessive car dependence compounded by "
                "inadequate planning. A coherent combination of superior public transport, charging "
                "mechanisms and sustainable urban design offers the most credible path to relief."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay provides a rigorous analysis of causes and a comprehensive, well-integrated "
                "set of solutions, all argued with sophistication and precision. The vocabulary is "
                "impressive, cohesion is seamless, and complex grammatical structures are used "
                "accurately throughout."
            ),
            "improvement_tips": [
                "No improvements required; this is a model band 9 response.",
            ],
        },
    },
    # ---------------- Q13: Obesity among young people (problem/solution) ----------------
    13: {
        "5": {
            "band": 5,
            "answer_text": (
                "Obesity is a big problem for young people in many countries. Many children are heavy "
                "because they eat bad food and do not play sports. This causes problems, and there are "
                "solutions.\n"
                "The problems are serious. Heavy children can get sick, for example they can have "
                "diabetes and heart problems when they grow up. They are also not happy because other "
                "children laugh at them. Some children cannot play sports with their friends, so they "
                "stay at home and watch television, and this makes them heavier.\n"
                "There are solutions. Parents should give their children healthy food like vegetables "
                "and fruit, and not many sweets and fast food. Schools should have more sports lessons, "
                "and children should play outside every day. For example, in my country, the "
                "government started a program for school sports, and many children became healthier. "
                "Television and computer games should also be limited.\n"
                "In conclusion, obesity makes young people sick and unhappy, but if parents, schools "
                "and governments work together, children can be healthy again."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response identifies problems and offers a range of solutions with a relevant "
                "example. The structure is clear, and the language is simple but generally accurate. "
                "The vocabulary is basic and the arguments are not deeply developed."
            ),
            "improvement_tips": [
                "Use more precise vocabulary: 'obesity', 'sedentary lifestyle', 'nutrition'.",
                "Develop each problem and solution in more detail.",
                "Use a wider range of linking words.",
                "Improve grammatical variety with conditionals and modal verbs.",
                "Ensure each paragraph has a clear topic sentence.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Rising rates of obesity among young people have become a pressing public health concern "
                "in many nations. This essay will explore the problems this trend creates and suggest "
                "measures that could help reverse it.\n"
                "The consequences of childhood obesity are far-reaching. Physically, overweight young "
                "people face a greatly increased risk of chronic conditions such as type 2 diabetes, "
                "heart disease and joint problems, both in adolescence and later life. There are also "
                "psychological effects: obese children are more likely to suffer from low self-esteem "
                "and bullying, which can lead to depression and social withdrawal. In the long term, "
                "these health issues place a substantial burden on healthcare systems and reduce "
                "quality of life.\n"
                "Several measures could address this problem. At home, parents should model and "
                "encourage healthy eating, limiting sugary drinks and processed snacks while ensuring "
                "regular family meals. Schools can play a central role by providing nutritious "
                "lunches, increasing the time devoted to physical education and teaching children "
                "about nutrition. Governments could also take action, for example by taxing unhealthy "
                "foods, subsidising fruit and vegetables, and restricting the advertising of junk "
                "food to children.\n"
                "In my view, the most effective approach combines all three levels of action, since "
                "parents, schools and governments each influence children's habits in different ways. "
                "A coordinated strategy is far more likely to succeed than isolated efforts.\n"
                "In conclusion, childhood obesity causes serious physical and psychological harm, but "
                "it is preventable. Through the combined efforts of families, schools and governments, "
                "young people can be encouraged to lead healthier, more active lives."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay clearly outlines the problems caused by obesity and proposes a well-reasoned "
                "range of solutions across different levels. It is logically organised and cohesive, "
                "with appropriate vocabulary. It could benefit from more specific data or examples."
            ),
            "improvement_tips": [
                "Include specific statistics or a named study to strengthen credibility.",
                "Use more advanced vocabulary such as 'sedentary lifestyle', 'public health burden' and 'preventive measures'.",
                "Vary sentence structures for sophistication.",
                "Make the introduction more precise about the scope of the essay.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The alarming escalation of obesity among the young constitutes one of the most serious "
                "public health challenges of the century, with prevalence rates rising steadily across "
                "both developed and developing nations. This essay will examine the manifold problems "
                "attendant upon this trend and propose a multi-layered programme of interventions.\n"
                "The harms wrought by childhood obesity are both physical and psychosocial, and their "
                "repercussions are enduring. Physiologically, obesity in adolescence markedly elevates "
                "the risk of type 2 diabetes, cardiovascular disease and musculoskeletal disorders, "
                "conditions once confined to adulthood but now emerging with alarming frequency in "
                "younger populations. Psychologically, the stigma associated with excess weight often "
                "engenders low self-esteem, anxiety and depression, frequently compounded by bullying "
                "and social exclusion. The cumulative consequence is a generation burdened with "
                "reduced life expectancy and an overstretched healthcare system.\n"
                "The solutions demand coordinated action across the multiple environments that shape a "
                "child's life. Within the home, parents can exert a profound influence by normalising "
                "nutritious diets, curtailing the consumption of ultra-processed foods and embedding "
                "activity into daily routines. Schools, as the institutions that hold young people for "
                "the largest proportion of their waking hours, must reinstate physical education as a "
                "priority, offer meals that are both healthy and appealing, and integrate nutrition "
                "literacy into the curriculum. At the policy level, governments possess powerful "
                "levers: fiscal measures such as sugar taxes, regulations restricting junk-food "
                "marketing directed at minors, and investment in public amenities that make active "
                "travel and outdoor recreation safe and accessible.\n"
                "I would argue that no single intervention is sufficient; the obesity epidemic is the "
                "product of a system, and it can only be reversed through systemic change. The most "
                "promising strategy unites families, schools and governments in a coherent, "
                "long-term campaign rather than relying on isolated, short-term programmes.\n"
                "In conclusion, the problems caused by rising obesity among young people are severe "
                "and compounding, yet they are by no means inevitable. A sustained, coordinated "
                "approach addressing diet, activity and the food environment offers the most credible "
                "route to safeguarding the health of future generations."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay delivers a comprehensive analysis of the physical and psychological harms of "
                "obesity and proposes a coherent, multi-level set of solutions. The argumentation is "
                "sophisticated, the vocabulary precise and varied, and the grammatical control "
                "flawless throughout."
            ),
            "improvement_tips": [
                "No improvement necessary at this level.",
            ],
        },
    },
    # ---------------- Q14: Plastic waste (problem/solution) ----------------
    14: {
        "5": {
            "band": 5,
            "answer_text": (
                "Plastic is everywhere, and it is a big problem for the environment. Plastic waste goes "
                "into the ocean, and animals eat it. This problem has causes and solutions.\n"
                "The problems are very serious. When plastic goes into the sea, fish and turtles eat it "
                "and they die. Also, plastic does not break down, so it stays in the environment for "
                "hundreds of years. For example, there is a big island of plastic in the ocean, and it "
                "is very dangerous for animals. Plastic also makes the beaches dirty and ugly.\n"
                "There are solutions. Companies should use less plastic for their products. They can "
                "use paper or glass instead. Governments can make a law to stop using plastic bags, and "
                "people can bring their own bags to the shop. Also, people should recycle plastic and "
                "not throw it in the street. Schools can teach children about the environment.\n"
                "In conclusion, plastic waste kills animals and pollutes nature, but if governments, "
                "companies and people work together, we can reduce this problem."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response identifies environmental problems and proposes several plausible solutions. "
                "The language is simple with basic vocabulary, and the structure is clear. The example "
                "of the plastic island is relevant but could be developed."
            ),
            "improvement_tips": [
                "Use more precise vocabulary: 'pollution', 'decomposition', 'biodegradable'.",
                "Develop each point in a fuller paragraph.",
                "Use more advanced connectors and varied sentence structure.",
                "Improve grammatical accuracy, especially verb forms.",
                "Make the conclusion more impactful.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Plastic pollution has become one of the most urgent environmental crises of our time, "
                "with vast quantities of waste accumulating in oceans, rivers and on land. This essay "
                "will outline the problems created by plastic waste and examine solutions that could "
                "mitigate the damage.\n"
                "The problems associated with plastic are severe and wide-ranging. In marine "
                "environments, plastic debris is frequently mistaken for food by fish, turtles and "
                "seabirds, causing injury and death, while microplastics have entered the food chain "
                "and are now found in drinking water and human bodies. Because plastic does not "
                "biodegrade, it persists for centuries, fragmenting into ever smaller particles that "
                "contaminate ecosystems. Beyond the environmental damage, plastic waste also imposes "
                "significant costs on communities through litter, blocked drainage and degraded "
                "coastal areas.\n"
                "Several solutions could reduce the problem. Companies should be encouraged, or "
                "required, to redesign packaging, favouring recyclable and biodegradable materials. "
                "Governments can introduce legislation banning single-use plastics and implement "
                "effective recycling programmes, as several countries have already done. Individuals "
                "also have a role to play by refusing unnecessary plastic, using reusable bags and "
                "bottles, and disposing of waste responsibly.\n"
                "In my view, the most successful strategies combine regulation with education and "
                "innovation. A ban on single-use plastics is most effective when accompanied by "
                "accessible alternatives and public awareness campaigns that change everyday habits.\n"
                "In conclusion, plastic waste causes serious harm to wildlife, ecosystems and human "
                "health, but the problem is far from insurmountable. Through the combined action of "
                "governments, businesses and individuals, plastic pollution can be dramatically "
                "reduced."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay clearly outlines the problems caused by plastic waste and proposes a coherent "
                "range of solutions involving different stakeholders. It is well organised and cohesive, "
                "with appropriate vocabulary. It could be enhanced with more specific, concrete examples."
            ),
            "improvement_tips": [
                "Add a specific example of a country that successfully reduced plastic use.",
                "Use more advanced vocabulary such as 'biodegradable', 'circular economy' and 'microplastics'.",
                "Vary complex sentence structures to add sophistication.",
                "Tighten the introduction for greater precision.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "Plastic waste has come to symbolise the environmental excesses of the modern age, "
                "pervading every ecosystem from the deepest ocean trenches to the most remote "
                "mountain peaks. This essay will analyse the manifold problems this material has "
                "created and evaluate the solutions available to stem the tide.\n"
                "The damage wrought by plastic pollution is both extensive and insidious. In marine "
                "systems, discarded plastic is ingested by creatures ranging from plankton to whales, "
                "inducing starvation, entanglement and death, while the degradation of larger items "
                "into microplastics has rendered contamination virtually irreversible at current "
                "levels of intervention. These particles have now permeated the food chain and are "
                "detectable in human bloodstreams, with the long-term health implications as yet "
                "unquantified. Economically, the consequences are equally tangible: coastal "
                "communities suffer diminished tourism, fisheries are compromised, and the cost of "
                "cleaning and managing waste falls heavily on the public purse.\n"
                "The solutions, while demanding, are achievable. At the production end, a transition "
                "towards a circular economy, in which packaging is designed for reuse and "
                "recyclability, is essential, supported by extended producer responsibility that "
                "compels manufacturers to internalise the environmental cost of their products. "
                "Legislative measures have proven their worth: bans on single-use plastics, adopted "
                "across the European Union and numerous other jurisdictions, have markedly reduced "
                "consumption, and the introduction of deposit-return schemes has driven recycling "
                "rates sharply upwards. Behavioural change, fostered through education and the "
                "provision of accessible alternatives, completes the triad, ensuring that "
                "sustainability becomes a habit rather than a gesture.\n"
                "I would contend, therefore, that the plastic crisis, although grave, is not "
                "intractable. Its resolution demands a systemic response that redesigns products, "
                "regulates markets and reshapes consumer behaviour in concert.\n"
                "In conclusion, plastic waste inflicts profound and lasting damage on the natural "
                "world and on human health, yet the levers to control it exist and have been shown to "
                "work. The challenge is one of collective will: to embed a circular economy, enforce "
                "sensible regulation and cultivate the everyday habits that will spare our "
                "environment from further degradation."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response provides a thorough, nuanced analysis of the problems of plastic "
                "pollution and a sophisticated, systemic set of solutions. The language is precise "
                "and varied, cohesion is seamless, and the grammatical range is extensive and "
                "consistently accurate."
            ),
            "improvement_tips": [
                "No improvements necessary at this level.",
            ],
        },
    },
    # ---------------- Q15: Fewer young people studying science (problem/solution) ----------------
    15: {
        "5": {
            "band": 5,
            "answer_text": (
                "In many countries, young people do not want to study science at university. They "
                "prefer other subjects. This is a problem for society, and there are solutions.\n"
                "Science is very important. We need scientists to make medicine, build bridges and "
                "invent new things. If young people do not study science, there will be no doctors and "
                "engineers in the future. For example, my country needs more engineers, but many "
                "students choose business because they think it is easy.\n"
                "Why do young people not choose science? They think science is difficult, and the "
                "lessons are boring. Also, science jobs are not always paid well, and parents do not "
                "encourage their children to study science.\n"
                "There are solutions. Schools can make science lessons more interesting with "
                "experiments and games. Governments can give more money to science students, like "
                "scholarships. Companies can pay scientists better salaries. Teachers can show "
                "students how science helps real life.\n"
                "In conclusion, fewer young people studying science is a serious problem, but if "
                "schools and governments act, more students will choose science in the future."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response addresses the problem, gives causes and proposes solutions, with a "
                "relevant example. The language is simple and the paragraphs are functional. Some "
                "sections (causes) are presented as a list rather than fully developed."
            ),
            "improvement_tips": [
                "Use a wider range of vocabulary: 'innovation', 'STEM subjects', 'career prospects'.",
                "Develop each idea in a full paragraph.",
                "Use more cohesive devices to link ideas.",
                "Improve grammatical accuracy and sentence variety.",
                "Tighten the focus on the societal consequences.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "A declining interest in science and technology among young people is a growing concern "
                "in many countries. This essay will examine the problems this trend creates for society "
                "and consider what can be done to reverse it.\n"
                "The consequences of a shortfall in science graduates are serious. Science and "
                "engineering drive innovation, and without a steady supply of qualified "
                "professionals, countries risk falling behind in medicine, technology and industry. "
                "Critical sectors such as healthcare, renewable energy and artificial intelligence "
                "already face skills shortages, and this is likely to worsen as demand grows. At a "
                "societal level, a weaker science workforce can undermine economic competitiveness and "
                "limit a nation's capacity to address major challenges such as climate change and "
                "disease.\n"
                "Several measures could encourage more students to study science. Schools should "
                "present the subjects in an engaging way, with hands-on experiments and links to "
                "real-world applications, rather than relying on rote learning. Governments could "
                "offer scholarships and bursaries to science students and fund research facilities "
                "that make the field more attractive. It is also important to raise the profile of "
                "science careers, showing young people that these professions are both rewarding and "
                "well paid.\n"
                "In my view, a combination of educational reform and financial incentives is most "
                "likely to succeed. If young people see science as exciting, relevant and rewarding, "
                "they will be far more inclined to pursue it.\n"
                "In conclusion, declining numbers of science students pose a serious threat to "
                "innovation and economic growth. Through more engaging teaching, financial support "
                "and improved career perceptions, governments can help rebuild interest in the "
                "sciences."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay clearly identifies the societal problems caused by declining interest in "
                "science and proposes sensible, well-explained solutions. It is logically organised "
                "and cohesive, with appropriate vocabulary. More specific examples would strengthen it."
            ),
            "improvement_tips": [
                "Include a specific statistic or example of a country's successful initiative.",
                "Use more advanced vocabulary such as 'technological literacy', 'incentivise' and 'workforce pipeline'.",
                "Vary sentence structures for greater sophistication.",
                "Make the conclusion more definitive.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The waning enthusiasm of young people for scientific disciplines is a phenomenon of "
                "considerable consequence, one whose implications ripple far beyond university "
                "campuses. This essay will examine the profound problems posed by this trend and "
                "assess the measures capable of reversing it.\n"
                "The societal costs of a diminished science workforce are substantial and "
                "multi-faceted. Innovation, the engine of modern economic growth, depends upon a "
                "pipeline of engineers, data scientists and researchers; a sustained shortfall "
                "therefore threatens national competitiveness and the capacity to address the defining "
                "challenges of the age, from pandemics to energy transition. The consequences are "
                "already visible in the acute shortages afflicting healthcare, semiconductors and "
                "renewable-energy industries, where vacancies remain unfilled for want of qualified "
                "graduates, and where the gap will widen as technological demand accelerates.\n"
                "The causes of this decline are as instructive as its consequences. Young people "
                "frequently perceive the sciences as intellectually inaccessible, and pedagogical "
                "approaches that privilege memorisation over discovery do little to dispel this "
                "impression. Moreover, a persistent mismatch between perceived and actual rewards "
                "discourages capable students, who are often drawn to fields perceived as more "
                "lucrative or prestigious. The absence of visible scientific role models compounds "
                "the problem, particularly for girls and minority groups.\n"
                "An effective response must therefore be systemic. Curricula should be redesigned to "
                "foreground inquiry, experimentation and the tangible relevance of science to everyday "
                "life, thereby demystifying the subject. Governments should deploy targeted financial "
                "instruments, including scholarships, loan forgiveness and research funding, that "
                "render science careers demonstrably attainable, while sustained media campaigns and "
                "mentorship programmes can reshape the public perception of scientists and engineers."
                "\n"
                "I would argue that this combination of pedagogical innovation, economic incentives "
                "and cultural reinforcement represents the most credible strategy for restoring the "
                "balance of talent towards the sciences.\n"
                "In conclusion, the retreat from science among the young imperils innovation, "
                "economic vitality and society's capacity to confront future crises. Yet the causes "
                "are identifiable and the remedies available; with determined, coordinated action, "
                "interest in the sciences can be revived."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response offers a sophisticated analysis of the causes and consequences of "
                "declining interest in science and a well-integrated programme of solutions. The "
                "argumentation is precise and nuanced, the vocabulary is rich, and the grammatical "
                "control is flawless."
            ),
            "improvement_tips": [
                "No improvements necessary; this is a band 9 response.",
            ],
        },
    },
    # ---------------- Q16: Online shopping (positive/negative) ----------------
    16: {
        "5": {
            "band": 5,
            "answer_text": (
                "Online shopping is very popular now, and many shops in the street are closing. Some "
                "people think this is good, and some people think it is bad. I think it is mostly "
                "good.\n"
                "Online shopping is good because it is easy. People can buy anything from their "
                "phones, and the things come to their home. They do not need to go to the shop. "
                "For example, my mother buys everything online now, and she saves a lot of time. "
                "Also, online shops have many choices, and sometimes the things are cheaper.\n"
                "But there are also bad things. Many people work in shops, and when the shops close, "
                "they lose their jobs. Also, some people buy too much online and waste money. And "
                "when people shop online, the packaging makes a lot of rubbish.\n"
                "In my opinion, online shopping is a positive development because it is convenient, "
                "but we should remember the people who lose their jobs.\n"
                "In conclusion, online shopping is mostly good because it is fast and easy, but it "
                "has some problems that we need to think about."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response gives a clear opinion and considers both positive and negative aspects. "
                "The language is simple and the structure is clear, but the arguments are not deeply "
                "developed and the vocabulary is basic."
            ),
            "improvement_tips": [
                "Use more precise vocabulary: 'e-commerce', 'convenience', 'brick-and-mortar stores'.",
                "Develop each point in a full paragraph.",
                "Use more varied linking words.",
                "Improve grammatical range and accuracy.",
                "Make the conclusion more decisive and well-reasoned.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The rapid rise of online shopping has transformed retail, and its consequences are "
                "being felt on high streets around the world, where many traditional shops have been "
                "forced to close. In my view, this is overwhelmingly a positive development, although "
                "it is not without its drawbacks.\n"
                "The benefits of online shopping are considerable. For consumers, it offers "
                "unrivalled convenience: purchases can be made at any time, from any location, and "
                "delivered directly to the door, saving both time and effort. The range of choice is "
                "also far greater than any physical store can offer, and prices are often more "
                "competitive, which benefits those on limited budgets. For businesses, e-commerce "
                "opens access to national and international markets without the prohibitive costs of "
                "bricks-and-mortar premises.\n"
                "Nevertheless, the decline of the high street has real costs. Many retail workers "
                "have lost their jobs as shops close, and town centres have lost their vitality, "
                "affecting communities that relied on them. There are also environmental concerns, "
                "as packaging and delivery traffic increase, and consumers may be tempted into "
                "impulsive, excessive spending.\n"
                "On balance, I believe the advantages of online shopping outweigh the disadvantages. "
                "The key is to manage the transition fairly, supporting affected workers and "
                "addressing the environmental impact, so that the benefits of digital retail are "
                "shared rather than concentrated.\n"
                "In conclusion, while the growth of online shopping has displaced traditional "
                "retailers and created new challenges, its convenience, choice and affordability make "
                "it a positive development overall."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay takes a clear position on whether online shopping is positive or negative "
                "and supports it with well-organised arguments. The response is cohesive and the "
                "vocabulary is appropriate, though more specific examples would strengthen it."
            ),
            "improvement_tips": [
                "Add a specific example, such as the impact on a named town or a statistic about retail closures.",
                "Use more sophisticated vocabulary such as 'bricks-and-mortar', 'logistics' and 'retail transition'.",
                "Vary sentence structures to add sophistication.",
                "Tighten the conclusion for greater impact.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The ascendancy of e-commerce, which has consigned a significant proportion of "
                "traditional retail to history, represents one of the most consequential commercial "
                "transformations of our era. While this development is not unalloyed, I am persuaded "
                "that, on balance, it constitutes a positive evolution for consumers, businesses and "
                "society at large.\n"
                "The advantages of online commerce are decisive. For the consumer, it delivers "
                "unparalleled convenience and choice, collapsing the constraints of geography and "
                "opening hours and, through price transparency and comparison, frequently securing "
                "better value. For entrepreneurs, particularly small enterprises, the digital "
                "marketplace erodes the barriers of capital and location, permitting them to reach "
                "audiences that would previously have been beyond their grasp. The efficiency gains "
                "of the model, moreover, are mirrored in reduced overheads and expanded markets, "
                "fostering innovation across the retail sector.\n"
                "The dislocations, however, cannot be dismissed. The closure of high-street stores "
                "has cost jobs and emptied town centres of their social and economic vitality, "
                "leaving communities bereft and public space underutilised. The environmental ledger "
                "is also mixed: although consolidated delivery fleets can be efficient, the ubiquity "
                "of packaging and the accelerated turnover of goods exert pressures of their own. "
                "These are the costs of progress, but they are costs that can be actively managed.\n"
                "I would therefore argue that the appropriate response is not to lament the digital "
                "transition but to govern it well. Policies that support retraining and "
                "reemployment for displaced workers, regulate packaging and logistics, and "
                "repurpose vacant retail space can ensure that the benefits of e-commerce are "
                "distributed equitably.\n"
                "In conclusion, the shift towards online shopping is, on balance, a positive "
                "development, delivering profound gains in convenience, choice and market access. "
                "Its disruptive consequences are real, yet they are manageable through prudent "
                "policy, and the net effect on modern life is a decidedly beneficial one."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay presents a clear, well-argued position on the overall effect of online "
                "shopping, weighing benefits against costs with sophistication before reaching a "
                "considered conclusion. The language is precise, cohesion is seamless, and the "
                "grammatical range is extensive and accurate."
            ),
            "improvement_tips": [
                "No improvement required at this level.",
            ],
        },
    },
    # ---------------- Q17: People living longer (positive/negative) ----------------
    17: {
        "5": {
            "band": 5,
            "answer_text": (
                "People live longer now because medicine is better and food is better. Is this a good "
                "thing? I think it is good, but there are some problems.\n"
                "Living longer is good because people can spend more time with their family. "
                "Grandparents can see their grandchildren grow up. My grandfather is eighty years old, "
                "and he is very happy that he can play with his grandchildren. Also, old people have "
                "much experience, and they can teach young people many things.\n"
                "But there are also problems. When people live longer, the population of old people "
                "grows. This means the government must pay more money for pensions and hospitals. "
                "Also, some old people are sick and need care, and their children must take care of "
                "them, which is difficult if the children work.\n"
                "In my opinion, living longer is a good development because family time is precious, "
                "but governments must be ready to help old people.\n"
                "In conclusion, people living longer is mostly good, but it brings new challenges "
                "for families and governments."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response gives a clear opinion and discusses both positive and negative aspects. "
                "The personal example is relevant, and the structure is logical. The language is "
                "simple and the vocabulary range is limited."
            ),
            "improvement_tips": [
                "Use more precise vocabulary: 'life expectancy', 'aging population', 'welfare system'.",
                "Develop arguments in fuller paragraphs.",
                "Use more varied connectors and sentence structures.",
                "Improve grammatical accuracy.",
                "Strengthen the conclusion by linking it to the main points.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Thanks to advances in medicine, nutrition and sanitation, people today live "
                "considerably longer than previous generations. While this is clearly a welcome "
                "development, it also brings significant challenges that deserve attention.\n"
                "There are strong reasons to view increased longevity as positive. Longer lives allow "
                "people to spend more time with family, to pursue their interests in retirement and to "
                "continue contributing their knowledge and experience to society. Older people are a "
                "valuable source of wisdom, and many remain active and productive well into their "
                "eighties. From a personal perspective, the prospect of a longer, healthier life is "
                "almost universally desired.\n"
                "However, longer lifespans also create difficulties. An ageing population places "
                "growing pressure on pension systems, healthcare services and social care, since older "
                "people generally require more medical attention and support. This burden falls "
                "ultimately on a smaller working-age population, who must fund these services through "
                "taxes. In some countries, the shortage of carers for the elderly has already become a "
                "serious issue, and families often struggle to balance work with caring for aged "
                "parents.\n"
                "In my view, increased longevity is undoubtedly a positive development, but it must "
                "be managed sensibly. Governments should plan for ageing populations by reforming "
                "pension systems, investing in healthcare and encouraging active ageing, so that "
                "longer lives are also healthy and productive ones.\n"
                "In conclusion, living longer is a positive achievement of modern society, bringing "
                "more time with family and continued contribution. Yet its sustainability depends on "
                "whether societies adapt their systems to support an ageing population."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay takes a clear position and balances the benefits of longevity against its "
                "challenges. It is well organised and cohesive, and the vocabulary is appropriate. "
                "More specific examples or data would strengthen the response."
            ),
            "improvement_tips": [
                "Include a specific example or statistic about ageing populations.",
                "Use more sophisticated vocabulary such as 'demographic shift', 'geriatric care' and 'sustainability'.",
                "Vary complex sentence structures to add sophistication.",
                "Make the conclusion more nuanced and memorable.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The extraordinary increase in human life expectancy, the product of medical progress, "
                "improved nutrition and public-health interventions, is one of the great triumphs of "
                "the modern age. Yet this achievement carries with it a set of consequences that are "
                "profoundly double-edged, and its overall value must be weighed with care.\n"
                "The benefits of longevity are self-evident and deeply human. Extended lifespans afford "
                "individuals more years with loved ones, greater opportunities for personal fulfilment "
                "in later life and the chance to witness the growth of subsequent generations. "
                "Societally, the accumulated wisdom of older citizens represents an invaluable "
                "resource, enriching communities, mentoring the young and preserving cultural "
                "continuity. For most people, the prospect of a long and healthy life is among the "
                "most cherished of aspirations.\n"
                "The costs, however, are equally substantial and increasingly pressing. Ageing "
                "populations impose mounting demands on pension systems, healthcare and long-term "
                "care, and with falling birth rates, these burdens fall on a shrinking workforce. The "
                "resulting fiscal strain threatens the viability of welfare states, while the "
                "practicalities of elder care strain families and often fall disproportionately on "
                "women. Moreover, a society with a very large elderly population and fewer young "
                "people may experience slower economic dynamism and diminished innovation.\n"
                "I would contend that increased longevity is fundamentally a positive development, "
                "but one whose promise can be realised only through foresight. It demands proactive "
                "reform of pension and healthcare systems, investment in preventive medicine and "
                "active ageing, and a cultural shift that regards the elderly as contributors rather "
                "than burdens.\n"
                "In conclusion, the extension of human life is a blessing of unprecedented "
                "proportions, yet it is a blessing that must be husbanded. If societies adapt "
                "wisely, longer lives can be both happier and more productive; if they do not, the "
                "gift of time may itself become a burden."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay presents a sophisticated, balanced assessment of increased longevity, "
                "acknowledging both its profound benefits and its societal costs before reaching a "
                "measured conclusion. The language is eloquent and precise, cohesion is seamless, "
                "and the grammatical range is extensive and accurate."
            ),
            "improvement_tips": [
                "No improvement needed at this level.",
            ],
        },
    },
    # ---------------- Q18: English as a global language (positive/negative) ----------------
    18: {
        "5": {
            "band": 5,
            "answer_text": (
                "English is now the most important language in the world, and millions of people study "
                "it. I think this is a good thing, but some people worry about other languages.\n"
                "English is good because people from different countries can talk to each other. "
                "For example, when my cousin travels, she speaks English with people from other "
                "countries. English helps people find good jobs, because many companies want "
                "workers who speak English. Also, most information on the internet is in English, "
                "so people who know English can learn many things.\n"
                "But there is a problem. When everybody learns English, some small languages can "
                "die. For example, in some countries, children learn English at school and they "
                "forget their own language. This is sad because languages carry culture, stories "
                "and traditions.\n"
                "In my opinion, English is very useful, but we should also protect our own "
                "languages and cultures.\n"
                "In conclusion, English as a global language is mostly a positive development, "
                "because it connects people, but we must not forget our local languages."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response gives a clear opinion and considers both sides with a relevant example. "
                "The structure is logical and the language is simple. The vocabulary is basic and the "
                "ideas are not deeply developed."
            ),
            "improvement_tips": [
                "Use more precise vocabulary: 'global lingua franca', 'cultural heritage', 'dominance'.",
                "Develop each point in a fuller paragraph.",
                "Use more varied linking words and structures.",
                "Improve grammatical accuracy.",
                "Make the conclusion stronger and more balanced.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "English has become the dominant global language, spoken by hundreds of millions of "
                "people as a first or second language. While this brings substantial benefits, it also "
                "raises concerns about cultural and linguistic diversity. On balance, I believe the "
                "spread of English is a largely positive development.\n"
                "The advantages of a common language are considerable. English serves as a global "
                "lingua franca, enabling communication across borders in business, science, travel and "
                "diplomacy. This greatly facilitates international cooperation and gives individuals "
                "access to a vast body of knowledge, since much of the world's research and content "
                "is published in English. Proficiency in English also enhances career opportunities, "
                "as it is increasingly a requirement in multinational companies and academia.\n"
                "Nevertheless, the dominance of English is not without drawbacks. The most significant "
                "is the threat it poses to smaller languages, which may decline as younger generations "
                "adopt English, leading to the erosion of cultural heritage and traditional knowledge. "
                "There is also a risk of cultural homogenisation, as global English-speaking media "
                "spreads similar values and lifestyles around the world.\n"
                "In my view, these risks can be managed. English can coexist with local languages "
                "if governments support mother-tongue education and cultural institutions, as many "
                "countries already do. The key is to treat English as a tool of communication rather "
                "than a replacement for one's own language.\n"
                "In conclusion, the spread of English as a global language brings clear benefits in "
                "communication and opportunity. Although it poses risks to linguistic diversity, "
                "these can be mitigated through policies that protect local languages and cultures."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay takes a clear position and discusses both benefits and risks, concluding "
                "with a sensible recommendation. It is well organised and cohesive, with appropriate "
                "vocabulary. More specific examples would strengthen the response."
            ),
            "improvement_tips": [
                "Add a specific example of a language protection initiative.",
                "Use more sophisticated vocabulary such as 'lingua franca', 'cultural homogenisation' and 'mother-tongue education'.",
                "Vary sentence structures to add sophistication.",
                "Refine the introduction for greater precision.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The emergence of English as a de facto global lingua franca is a linguistic phenomenon "
                "without historical parallel, reshaping communication on every continent. Its spread "
                "confers indisputable benefits, yet it also carries consequences that demand a balanced "
                "appraisal. On the whole, I regard it as a positive development, provided that "
                "societies take deliberate steps to safeguard linguistic diversity.\n"
                "The practical advantages of a shared global tongue are immense. In an increasingly "
                "interconnected world, English facilitates the seamless exchange of ideas across "
                "borders in commerce, science, medicine and diplomacy, accelerating collaboration and "
                "innovation. It grants individuals access to an overwhelming proportion of the world's "
                "published knowledge and digital content, and fluency in it is a passport to "
                "international education and employment. For countless people, English is not a threat "
                "to their identity but a ladder to opportunity.\n"
                "The costs, however, are real and must not be dismissed. The ascendancy of English "
                "accelerates the decline of minority languages, many of which are vanishing as younger "
                "speakers gravitate towards the global tongue, taking with them irreplaceable bodies "
                "of oral literature, indigenous knowledge and distinct ways of seeing the world. The "
                "cultural gravitation towards English-speaking media also risks a homogenising effect, "
                "eroding local customs and creative industries that cannot compete on the global "
                "stage.\n"
                "I would argue that the remedy lies not in resisting English but in parallel "
                "reinforcement of native languages. Where governments fund mother-tongue education, "
                "celebrate vernacular literature and legislate for bilingual media, English can "
                "flourish as a functional tool without supplanting the languages through which "
                "communities express their deepest identity.\n"
                "In conclusion, the global spread of English is, on balance, a positive development, "
                "offering unprecedented access to communication and knowledge. Its potential to "
                "diminish linguistic diversity is real, yet it is a challenge that informed policy "
                "and cultural stewardship can successfully meet."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay delivers a nuanced and comprehensive assessment of English as a global "
                "language, balancing its benefits against its cultural costs and proposing a "
                "constructive path forward. The vocabulary is sophisticated, cohesion is seamless, "
                "and the grammatical range is extensive and accurate."
            ),
            "improvement_tips": [
                "No improvements necessary at this level.",
            ],
        },
    },
    # ---------------- Q19: Automation replacing jobs (positive/negative) ----------------
    19: {
        "5": {
            "band": 5,
            "answer_text": (
                "Machines and computers can now do many jobs that people used to do. Some people are "
                "happy, but other people are worried. I think this is both good and bad.\n"
                "Machines are good because they can do work faster and better than people. For "
                "example, in factories, robots can build cars in a short time, and they do not get "
                "tired. Machines also make things cheaper, so people can buy more things. Doctors "
                "also use machines to find diseases early.\n"
                "But machines are bad because many people lose their jobs. When a factory uses "
                "robots, the workers lose their work, and they cannot find new jobs easily. For "
                "example, in my city, many factory workers became jobless because of machines. "
                "These people have families and need money, but they do not know how to use new "
                "technology.\n"
                "In my opinion, automation is good for progress, but governments must help workers "
                "who lose their jobs, for example by teaching them new skills.\n"
                "In conclusion, machines and computers bring many good things, but they also take "
                "away jobs. We need to be careful and help people."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response discusses both positive and negative effects of automation with a "
                "relevant example. The language is simple and the structure is clear, but the "
                "arguments are not deeply developed and the vocabulary is basic."
            ),
            "improvement_tips": [
                "Use more precise vocabulary: 'automation', 'redundancy', 'retraining'.",
                "Develop each point in a fuller paragraph.",
                "Use more sophisticated connectors.",
                "Improve grammatical range and accuracy.",
                "Make the conclusion more analytical.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Automation and artificial intelligence are rapidly transforming the workplace, taking "
                "over tasks that were once the preserve of human workers. While this development brings "
                "considerable benefits, it also poses serious challenges. On balance, I believe it is a "
                "positive development, provided that the transition is managed responsibly.\n"
                "The benefits of automation are substantial. Machines can perform repetitive and "
                "dangerous tasks more safely and consistently than humans, reducing workplace "
                "accidents and improving quality. Automation also drives down costs, making goods and "
                "services more affordable and increasing productivity, which can create wealth and "
                "free people from tedious work. In fields such as medicine, automated systems can "
                "analyse data faster than doctors, aiding diagnosis and treatment.\n"
                "The negative consequences, however, are equally significant. The most immediate is "
                "job displacement, as automated systems replace workers in manufacturing, "
                "administration and even professional roles. Displaced workers, particularly those "
                "in middle age, often struggle to find new employment, especially if their skills "
                "are not transferable. This can lead to unemployment, economic hardship and social "
                "inequality, widening the gap between skilled and unskilled workers.\n"
                "In my view, automation itself is not the problem; the problem is how society "
                "adapts to it. Governments and businesses must invest in education and retraining "
                "programmes so that displaced workers can acquire the skills required for new "
                "types of employment, and consider measures such as income support during the "
                "transition.\n"
                "In conclusion, automation is a positive development overall, increasing efficiency "
                "and prosperity. Yet its benefits will be realised only if societies proactively "
                "support workers whose jobs are affected and prepare people for the changing nature "
                "of work."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay takes a clear, balanced position on automation and supports it with "
                "well-organised arguments. The response is cohesive and the vocabulary is appropriate. "
                "It could be strengthened with more specific examples and statistics."
            ),
            "improvement_tips": [
                "Include a specific statistic or example of automation's impact on a particular industry.",
                "Use more advanced vocabulary such as 'technological unemployment', 'reskilling' and 'labour displacement'.",
                "Vary complex sentence structures to add sophistication.",
                "Tighten the conclusion for greater force.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The accelerating capacity of machines and algorithms to perform tasks once "
                "exclusively human has inaugurated a new epoch of economic transformation. Although "
                "this development provokes legitimate anxiety, I am persuaded that it is, on balance, "
                "a positive development, whose success, however, hinges on the wisdom with which "
                "societies manage its disruptive effects.\n"
                "The gains from automation are profound and pervasive. Machines execute repetitive, "
                "hazardous and precision-critical tasks with a consistency beyond human capacity, "
                "elevating safety and quality while reducing costs that are ultimately passed to "
                "consumers. Freed from drudgery, workers can devote themselves to roles that demand "
                "creativity, empathy and judgement, the very capacities that machines cannot "
                "replicate. In healthcare, algorithmic analysis augments diagnosis and accelerates "
                "research; in industry, it underpins productivity growth that funds public services. "
                "The potential of automation to raise living standards across the world is immense."
                "\n"
                "Yet the transition exacts a heavy price that must be acknowledged. Displacement is "
                "not hypothetical: manufacturing, clerical and increasingly cognitive roles are "
                "ceding ground to automated systems, and displaced workers, especially those past "
                "mid-career, confront a labour market that offers them few footholds. Absent "
                "intervention, this dynamic widens inequality, concentrates wealth and generates "
                "widespread resentment towards technological progress.\n"
                "I would therefore argue that the character of automation's legacy will be "
                "determined by policy. Investment in education and lifelong retraining, the "
                "expansion of social safety nets to bridge transitions, and a reasoned debate about "
                "the distribution of the gains from productivity are all indispensable if the "
                "benefits of automation are to be shared rather than hoarded.\n"
                "In conclusion, automation is a decidedly positive development, promising "
                "unprecedented efficiency and the liberation of human potential. Whether it "
                "fulfils that promise, however, depends less on the machines themselves than on the "
                "collective wisdom with which we navigate the change they bring."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay provides a sophisticated and balanced treatment of automation, weighing its "
                "transformative benefits against its disruptive costs and concluding that its legacy "
                "depends on governance. The language is precise and eloquent, cohesion is seamless, "
                "and the grammatical range is extensive and accurate."
            ),
            "improvement_tips": [
                "No improvements required at this level.",
            ],
        },
    },
    # ---------------- Q20: Fast food popularity (double question) ----------------
    20: {
        "5": {
            "band": 5,
            "answer_text": (
                "Fast food is very popular with young people all over the world. They love hamburgers, "
                "pizza and fried chicken. In this essay, I will say why fast food is popular and how "
                "to make young people eat healthily.\n"
                "Fast food is popular for many reasons. First, it is very cheap, so young people can "
                "buy it with their pocket money. Second, it is fast, so they can eat it between "
                "classes or activities. Third, fast food tastes good, because it has a lot of sugar "
                "and salt. Also, there are fast food restaurants everywhere, and they are always "
                "open.\n"
                "To make young people eat healthily, we can do many things. Schools can teach "
                "students about healthy food in their lessons. Parents can cook healthy food at home "
                "and not buy fast food often. Schools can also sell healthy food like fruit and "
                "salads instead of chips and sweets. Governments can make fast food more expensive "
                "and healthy food cheaper.\n"
                "In conclusion, fast food is popular because it is cheap, fast and tasty, but "
                "parents, schools and governments can help young people choose healthier food."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "Both parts of the question are addressed: reasons for popularity and measures to "
                "encourage healthier eating. The response is clearly structured with lists of ideas, "
                "though the language is simple and the ideas are not deeply developed."
            ),
            "improvement_tips": [
                "Use more precise vocabulary: 'convenience', 'nutrition', 'processed food'.",
                "Develop each reason and measure in fuller paragraphs.",
                "Use more sophisticated linking words.",
                "Improve grammatical range and accuracy.",
                "Ensure the conclusion clearly answers both parts of the question.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Fast food has become an entrenched feature of the diets of young people worldwide. "
                "This essay will examine why this food is so appealing to the young, and consider "
                "what measures could encourage them to adopt healthier eating habits.\n"
                "There are several reasons for the popularity of fast food among young people. The "
                "most important is convenience: burgers, fried chicken and pizza can be obtained "
                "quickly and eaten on the move, which suits the fast-paced lifestyle of students. "
                "Cost is another factor, as fast food is often cheaper than a healthier restaurant "
                "meal, making it attractive to those with limited budgets. In addition, fast food "
                "is heavily advertised and engineered to be highly palatable, with combinations of "
                "salt, sugar and fat that appeal strongly to young taste buds. Social pressure also "
                "plays a role, since fast food restaurants are popular places for young people to "
                "meet.\n"
                "A number of measures could encourage healthier eating. Schools can play a central "
                "role by providing nutritious meals and teaching students about nutrition, while "
                "restricting the sale of junk food on school premises. Parents can model healthy "
                "habits and limit how often children eat fast food. Governments could also act by "
                "taxing sugary and high-fat products, funding public health campaigns and "
                "restricting the advertising of fast food to children.\n"
                "In my view, the most effective approach combines education with regulation. If "
                "young people understand the consequences of their choices and are presented with "
                "affordable healthy alternatives, they are far more likely to change their habits.\n"
                "In conclusion, fast food is popular because it is quick, cheap and appealing, but "
                "a combination of school education, parental guidance and government regulation can "
                "help steer young people towards healthier diets."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay addresses both parts of the question thoroughly and coherently, offering "
                "well-developed reasons and practical measures. The vocabulary is appropriate and "
                "the response is logically organised. Specific examples would strengthen it further."
            ),
            "improvement_tips": [
                "Add a concrete example or statistic about fast food consumption among the young.",
                "Use more advanced vocabulary such as 'palatability', 'dietary habits' and 'public health campaigns'.",
                "Vary complex sentence structures to add sophistication.",
                "Tighten the conclusion so it clearly answers both questions.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The pervasive appeal of fast food among younger generations has become a subject of "
                "considerable public concern, given its association with obesity and chronic disease. "
                "This essay will explore the reasons underpinning this popularity and evaluate the "
                "measures most likely to foster healthier eating among the young.\n"
                "The popularity of fast food is attributable to a confluence of factors. Chief among "
                "them is convenience: in an era of packed schedules, the immediacy of a meal that is "
                "ordered and consumed in minutes offers an irresistible pragmatic advantage. Its "
                "affordability, moreover, positions it within reach of the limited budgets of "
                "students, and its consistent, aggressively marketed flavour profiles are "
                "deliberately calibrated to exploit innate human preferences for fat, sugar and "
                "salt. These attributes are amplified by the social dimension of fast food, which "
                "functions as a gathering place for adolescents, and by omnipresent advertising that "
                "normalises its consumption.\n"
                "Combating this phenomenon requires an equally multi-faceted response. In schools, "
                "nutrition education should be embedded not as an abstract subject but as practical "
                "life skills, and the food environment itself must be reformed so that healthy "
                "options are the default rather than the exception. Parents exercise profound "
                "influence through the habits they model and the boundaries they set, establishing "
                "expectations that endure into adulthood. At the policy level, fiscal measures such "
                "as levies on sugar-sweetened beverages, coupled with restrictions on marketing to "
                "minors and subsidies that make fresh produce affordable, have demonstrated "
                "measurable success in altering consumption patterns.\n"
                "I would argue that no single lever is sufficient; the dietary habits of a "
                "generation are shaped by a system of incentives, availability and culture, and it "
                "is this system that must be reformed. The most promising strategies therefore "
                "integrate education, environmental change and regulation into a coherent whole.\n"
                "In conclusion, the dominance of fast food among the young reflects deep-seated "
                "forces of convenience, cost, biology and socialisation. Reversing it demands an "
                "equally comprehensive approach, one that makes healthy choices easier, more "
                "affordable and more appealing than the alternatives."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay answers both parts of the question with sophistication, analysing the "
                "reasons for fast food's popularity and proposing a coherent, multi-level set of "
                "measures. The language is precise and varied, cohesion is seamless, and the "
                "grammatical range is extensive and accurate."
            ),
            "improvement_tips": [
                "No improvement necessary at this level.",
            ],
        },
    },
    # ---------------- Q21: Rise of remote learning (double question) ----------------
    21: {
        "5": {
            "band": 5,
            "answer_text": (
                "More and more students are learning online now instead of going to school. This "
                "essay will talk about why online learning is popular and what effects it has.\n"
                "Online learning is popular because it is convenient. Students can study from home "
                "and they do not need to travel to school. They can also choose the time to study, "
                "so they can work or help their family. For example, my cousin studies online in the "
                "evening because he works during the day. Also, online courses are sometimes cheaper "
                "than normal school.\n"
                "Online learning has effects on students and teachers. Students can learn at their "
                "own speed and watch the lessons again. But some students feel lonely because they "
                "do not see their classmates. It is also difficult for teachers because they cannot "
                "see if the students are listening. Some students do not have good internet, so they "
                "cannot join the class.\n"
                "In conclusion, online learning is popular because it is easy and flexible, but it "
                "makes students feel lonely and is difficult for teachers."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "Both parts of the question are addressed, with reasons for popularity and effects on "
                "students and teachers. The response is clearly organised, but the language is simple "
                "and the effects are described rather than developed."
            ),
            "improvement_tips": [
                "Use more precise vocabulary: 'flexibility', 'remote instruction', 'digital divide'.",
                "Develop each effect with more explanation and examples.",
                "Use a wider range of linking words.",
                "Improve grammatical accuracy and variety.",
                "Strengthen the conclusion by summarising both parts clearly.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Remote learning has expanded rapidly in recent years, and for many students it has "
                "become the norm rather than the exception. This essay will consider why online "
                "education has grown so popular and examine its effects on students and teachers.\n"
                "The popularity of online learning can be attributed to several factors. Above all, "
                "it offers remarkable flexibility: students can study from anywhere and at times "
                "that suit them, which is invaluable for those who also work or care for family. "
                "Cost is another consideration, as online courses are often more affordable than "
                "traditional programmes, and the technology has made high-quality education "
                "accessible to people in remote or underserved areas. The COVID-19 pandemic also "
                "accelerated acceptance of the model, normalising remote instruction for millions.\n"
                "The effects of this shift have been mixed. For students, online learning can "
                "foster independence and self-discipline, and recorded lessons allow them to learn "
                "at their own pace. However, many students experience isolation and find it harder "
                "to stay motivated, and those without reliable internet or suitable devices are "
                "disadvantaged, deepening educational inequality. For teachers, remote delivery "
                "demands new skills and makes it harder to gauge understanding, while the absence "
                "of face-to-face contact can reduce the rapport that supports learning.\n"
                "In my view, online learning is a valuable complement to traditional education "
                "rather than a complete replacement. A blended approach that combines the "
                "flexibility of online study with the social and interactive benefits of the "
                "classroom is likely to serve students best.\n"
                "In conclusion, online learning has grown popular because of its flexibility and "
                "accessibility, and it offers real benefits for students and teachers. Yet its "
                "drawbacks, including isolation and inequality, suggest that a balanced, blended "
                "model is the most sensible way forward."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay addresses both parts of the question coherently, explaining the reasons for "
                "online learning's popularity and analysing its effects on students and teachers. The "
                "response is well organised and cohesive, with appropriate vocabulary. It could be "
                "strengthened with specific examples."
            ),
            "improvement_tips": [
                "Include a specific example, such as a country's experience with online schooling.",
                "Use more advanced vocabulary such as 'digital divide', 'pedagogical challenges' and 'blended learning'.",
                "Vary sentence structures to add sophistication.",
                "Tighten the conclusion for greater impact.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The meteoric rise of online learning has reconfigured the educational landscape, "
                "sweeping millions of students out of traditional classrooms and into digital "
                "lecture halls. This essay will explore the forces driving this transformation and "
                "assess its implications for both learners and educators.\n"
                "The ascendancy of remote education rests on a foundation of profound "
                "practicality. Its defining virtue is flexibility: liberated from the constraints of "
                "geography and the clock, students can tailor their study to the rhythms of work "
                "and family, an accommodation that conventional schooling cannot offer. Economic "
                "forces reinforce this appeal, as online programmes frequently undercut the costs "
                "of campus-based study and extend access to those in rural and underserved "
                "communities. The pandemic, moreover, functioned as a forcing mechanism, "
                "compelling institutions worldwide to develop and refine digital pedagogies, and "
                "thereby permanently expanding the expectations of what education can be.\n"
                "The consequences of this shift are as complex as they are consequential. For many "
                "students, online learning cultivates autonomy, digital fluency and the capacity "
                "for self-directed inquiry, while the availability of recorded material permits "
                "genuinely personalised pacing. Yet these benefits are unequally distributed: "
                "students lacking connectivity or quiet study space are systematically "
                "disadvantaged, and the erosion of social contact can impair motivation, "
                "wellbeing and the development of interpersonal skills. Teachers, too, face a "
                "transformed profession, in which assessing genuine understanding without "
                "physical cues, and maintaining engagement across a screen, demand skills for "
                "which few were trained.\n"
                "I would contend that the future of education lies not in the wholesale "
                "replacement of the classroom but in its augmentation. A blended model, which "
                "harnesses the flexibility of online learning while preserving the irreplaceable "
                "value of human interaction, appears best suited to deliver both access and "
                "quality.\n"
                "In conclusion, the popularity of online learning is a product of its remarkable "
                "flexibility and accessibility, and its effects on students and teachers are "
                "profoundly double-edged. Managed thoughtfully, it enriches education; neglected, "
                "it risks widening the very divides it once promised to close."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay addresses both parts of the question with exceptional depth and nuance, "
                "analysing the drivers of online learning and its complex effects on students and "
                "teachers. The language is sophisticated and precise, cohesion is seamless, and the "
                "grammatical range is extensive and accurate."
            ),
            "improvement_tips": [
                "No improvements necessary at this level.",
            ],
        },
    },
    # ---------------- Q22: International travel growth (double question) ----------------
    22: {
        "5": {
            "band": 5,
            "answer_text": (
                "More and more people are travelling to other countries now. This essay will talk "
                "about why people travel more and what effects this has on the countries they "
                "visit.\n"
                "People travel more because it is easier and cheaper now. Airplanes are fast, and "
                "there are many cheap flights. For example, my family went to another country for "
                "a holiday, and the tickets were not expensive. Also, people can find information "
                "about travel on the internet, and they can book hotels and flights online. "
                "Many people also want to see famous places and learn about other cultures.\n"
                "Travel has good and bad effects on the countries people visit. The good effect is "
                "that tourists bring money, so the country's economy grows. Hotels and restaurants "
                "get more customers, and people find jobs in tourism. But there are also bad "
                "effects. Popular places can become very crowded, and the environment can be "
                "damaged. For example, in some countries, beautiful beaches have too many tourists, "
                "and the sea becomes dirty.\n"
                "In conclusion, people travel more because it is easy and cheap, and tourism brings "
                "money to countries, but it can also cause problems for the environment."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "Both parts of the question are addressed: reasons for increased travel and effects on "
                "destination countries. The response is clearly structured with a relevant example, "
                "but the language is simple and the ideas are not deeply developed."
            ),
            "improvement_tips": [
                "Use more precise vocabulary: 'tourism', 'economy', 'cultural exchange'.",
                "Develop each point in a fuller paragraph.",
                "Use more varied linking words and structures.",
                "Improve grammatical accuracy.",
                "Strengthen the conclusion by summarising both parts.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "International travel has grown enormously in recent decades, as rising incomes and "
                "cheaper transport have put foreign holidays within reach of millions. This essay "
                "will examine why more people are travelling abroad and consider the effects of this "
                "trend on the countries they visit.\n"
                "Several factors explain the growth in international travel. Affordability is "
                "central: the expansion of low-cost airlines and package holidays has made flying "
                "far cheaper than it once was, while the internet allows travellers to compare "
                "prices and book easily. Rising living standards mean that more people can afford "
                "to spend on leisure, and increased exposure to travel content online has created "
                "a strong desire to experience other cultures and see famous landmarks. Improved "
                "safety and visa procedures have also reduced the barriers to visiting foreign "
                "countries.\n"
                "The effects on destination countries are mixed. The most obvious benefit is "
                "economic: tourism generates significant revenue, creates jobs in hotels, "
                "restaurants and transport, and can support the preservation of historic sites. It "
                "also encourages cultural exchange and international understanding. However, "
                "mass tourism can place enormous pressure on local infrastructure and the "
                "environment. Popular destinations suffer from overcrowding, pollution and the "
                "damage of fragile ecosystems, while rising prices can make housing and goods "
                "unaffordable for local residents.\n"
                "In my view, international travel is generally a positive force, provided it is "
                "managed sustainably. Governments should invest in managing visitor numbers and "
                "promoting responsible tourism so that the benefits are preserved without "
                "destroying the very places people come to see.\n"
                "In conclusion, people travel abroad more because travel has become cheaper, easier "
                "and more appealing, and this brings both economic benefits and environmental "
                "challenges to host countries. With sensible management, the advantages of "
                "international travel can be maximised."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay addresses both parts of the question thoroughly, explaining the reasons for "
                "increased travel and analysing the benefits and drawbacks for host countries. It is "
                "well organised and cohesive, with appropriate vocabulary, though specific examples "
                "would strengthen it."
            ),
            "improvement_tips": [
                "Add a specific example, such as a destination affected by mass tourism.",
                "Use more advanced vocabulary such as 'overtourism', 'sustainable tourism' and 'cultural exchange'.",
                "Vary complex sentence structures to add sophistication.",
                "Tighten the conclusion to answer both questions clearly.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The surge in international travel, propelled by economic growth and the "
                "democratisation of air travel, has become one of the defining social phenomena of "
                "the contemporary era. This essay will account for the rising propensity to travel "
                "abroad and assess the manifold effects of this trend upon destination nations.\n"
                "The proliferation of foreign travel owes much to a convergence of economic and "
                "technological forces. The liberalisation of aviation and the advent of low-cost "
                "carriers have collapsed the cost of international flights, transforming travel "
                "from a luxury into an accessible pursuit. Concurrently, rising disposable incomes "
                "in both developed and emerging economies have expanded the pool of prospective "
                "travellers, while digital platforms have simplified every stage of the journey, "
                "from comparison and booking to navigation. These practical drivers are reinforced "
                "by a cultural appetite, cultivated by social media, for authentic experiences and "
                "encounters with the unfamiliar.\n"
                "The consequences for host countries are profound and ambivalent. On the economic "
                "ledger, tourism is a formidable engine: it stimulates employment, generates "
                "foreign exchange and often finances the conservation of heritage. Its cultural "
                "dimension is equally valuable, fostering exchange and mutual understanding "
                "between peoples. Yet the costs are commensurate: the phenomenon of overtourism "
                "strains infrastructure, drives up living costs for residents and imperils "
                "fragile environments, while the commodification of local culture can erode "
                "authenticity. The economic dependence on a volatile sector also exposes "
                "communities to sudden shocks.\n"
                "I would argue that international travel is, on balance, a force for good whose "
                "excesses can be contained through deliberate stewardship. Visitor management, "
                "investment in sustainable infrastructure and the cultivation of responsible "
                "tourism can reconcile the economic rewards with the preservation of the "
                "destinations concerned.\n"
                "In conclusion, the growth of international travel stems from profound changes in "
                "affordability, technology and aspiration, and its effects on host countries are "
                "simultaneously beneficial and burdensome. The challenge of our time is to "
                "harness its advantages while safeguarding the places and cultures it celebrates."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay addresses both parts of the question with sophistication, analysing the "
                "drivers of increased travel and its complex effects on destination countries. The "
                "language is precise and eloquent, cohesion is seamless, and the grammatical range "
                "is extensive and accurate."
            ),
            "improvement_tips": [
                "No improvement required at this level.",
            ],
        },
    },
    # ---------------- Q23: Teenagers and part-time jobs (double question) ----------------
    23: {
        "5": {
            "band": 5,
            "answer_text": (
                "Many teenagers work part-time at weekends and in the holidays. This essay will talk "
                "about why teenagers work and the good and bad things about it.\n"
                "Teenagers work part-time for many reasons. Some work because they want money to buy "
                "things like phones and clothes, or to go out with their friends. Some want to help "
                "their family with money. Others work because they want to learn new skills and "
                "have experience for their future. For example, my brother works in a restaurant, "
                "and he learns how to talk to customers.\n"
                "There are good things about part-time work. Teenagers learn to be responsible and "
                "to manage their money. They also learn new skills, like working in a team. But "
                "there are also bad things. If teenagers work too many hours, they are tired and "
                "cannot study well. They have less time for homework and for their friends. Some "
                "jobs are also dangerous or not good for young people.\n"
                "In conclusion, teenagers work part-time for money, for their family and for "
                "experience. It has good effects, like learning skills, but it can also be bad if "
                "they work too much."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "Both parts of the question are addressed: reasons for working and the advantages and "
                "risks. The response is clearly structured with a relevant example, but the language "
                "is simple and the arguments are not deeply developed."
            ),
            "improvement_tips": [
                "Use more precise vocabulary: 'work experience', 'financial independence', 'responsibilities'.",
                "Develop each advantage and risk in a fuller paragraph.",
                "Use more varied linking words.",
                "Improve grammatical accuracy and variety.",
                "Make the conclusion more analytical.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "Part-time employment among teenagers has become common in many countries, with young "
                "people taking jobs in shops, restaurants and other local businesses. This essay "
                "will examine why teenagers choose to work and weigh the advantages against the "
                "potential risks.\n"
                "Teenagers take part-time jobs for a variety of reasons. For many, the primary "
                "motive is financial: part-time work provides pocket money for leisure, clothes and "
                "technology, and it can also teach the value of money. Some teenagers contribute "
                "this income to their families, while others are motivated by the desire to gain "
                "work experience that will strengthen their university applications and future "
                "careers. Social reasons also play a part, as working with colleagues can be an "
                "enjoyable and rewarding experience.\n"
                "The advantages of part-time work are considerable. It instils responsibility, "
                "time management and interpersonal skills that classroom education rarely "
                "teaches, and it offers a first taste of financial independence. However, there "
                "are also risks. Excessive working hours can interfere with schoolwork, leaving "
                "teenagers exhausted and unable to keep up with their studies. The pressures of "
                "work can also reduce the time available for rest, hobbies and family, and some "
                "jobs may expose young people to inappropriate environments or demands.\n"
                "In my view, part-time work is beneficial for teenagers when it is balanced. A "
                "reasonable number of hours, typically at weekends and holidays, allows young "
                "people to gain valuable experience without jeopardising their education or "
                "wellbeing.\n"
                "In conclusion, teenagers work part-time for money, experience and independence, "
                "and the practice offers genuine benefits in responsibility and skills. Provided "
                "working hours are kept sensible, these advantages can be enjoyed without the "
                "associated risks."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The essay addresses both parts of the question clearly, explaining why teenagers work "
                "and analysing the advantages and risks. It is well organised and cohesive, with "
                "appropriate vocabulary. More specific examples would strengthen the response."
            ),
            "improvement_tips": [
                "Add a concrete example of a typical part-time job and its benefits or drawbacks.",
                "Use more advanced vocabulary such as 'work-life balance', 'financial literacy' and 'extracurricular'.",
                "Vary complex sentence structures to add sophistication.",
                "Tighten the conclusion to answer both parts explicitly.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The prevalence of part-time employment among teenagers is a familiar feature of "
                "many societies, yet its wisdom is the subject of perennial debate. This essay will "
                "explore the motivations that draw young people into the workforce and evaluate the "
                "benefits and hazards that accompany early employment.\n"
                "The reasons compelling teenagers to seek part-time work are various and, in most "
                "cases, pragmatic. Financial independence is a primary incentive: employment confers "
                "disposable income, enabling young people to fund their own leisure and purchases, "
                "and in doing so imparts an early appreciation of the relationship between effort "
                "and reward. For others, part-time work is a strategic investment, offering "
                "workplace experience, references and a demonstration of responsibility that "
                "enhance university admissions and future employability. The social dimension, "
                "too, should not be discounted, for many adolescents find genuine satisfaction in "
                "the camaraderie and responsibility of the workplace.\n"
                "The benefits of early employment are, nevertheless, accompanied by genuine "
                "hazards. Prolonged working hours, particularly when they encroach upon evenings "
                "and weekends, can erode academic performance through fatigue and the "
                "displacement of study time. The developmental costs extend beyond the academic, "
                "as relentless schedules can curtail the rest, hobbies and unstructured social "
                "interaction that are integral to healthy adolescence. Certain industries, "
                "moreover, expose young workers to demands for which their maturity may not yet "
                "equip them.\n"
                "I would contend that part-time work is neither inherently virtuous nor inherently "
                "harmful; its effects are determined by its scale and context. Employment that "
                "is moderate in hours, genuinely instructive and respectful of a teenager's "
                "educational obligations confers clear benefits, whereas excessive or exploitative "
                "work inflicts corresponding harm.\n"
                "In conclusion, teenagers are drawn to part-time jobs by considerations of money, "
                "experience and independence, and such work can be a formative and rewarding "
                "experience. Its value, however, hinges upon balance, for the very benefits it "
                "bestows are forfeited when it encroaches upon the education and wellbeing of the "
                "young."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "The essay addresses both parts of the question with sophistication, analysing the "
                "reasons for teenage employment and evaluating its benefits and hazards in a "
                "measured, nuanced conclusion. The language is precise and elegant, cohesion is "
                "seamless, and the grammatical range is extensive and accurate."
            ),
            "improvement_tips": [
                "No improvements necessary at this level.",
            ],
        },
    },
}
