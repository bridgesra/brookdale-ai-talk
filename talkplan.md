I have a roughly outline here for the talk. I want you to help me make it into a clear description of what goes on each slide and what to say. then I'll build the slides. I tried to mention what I think the titles should be and what should be on the slides. I also included dialogue which i'll put in the notes and give you a feel for the talk. Return a structured set of title, content, notes/dialogue for each slide. criticise and make better. ask questions if needed. From that outline I'll make actual slides, right now we're making the detailed plan.

## Title slide
AI: How it works, what it can do, and what we should worry about
An introduction and discussion for Brookdale residents

Robert “Bobby” Bridges
Mary Bridges’s son
PhD, AI & Security Research and Innovation Leader, AI Sweden 
[use one of the AI Sweden logos in aise-logos here by my organization name]

## Next slide: Slide 2 — AI learns patterns to make predictions
On the slide

Large central statement:

Modern AI learns patterns from examples and uses those patterns to make predictions.

Underneath, in smaller type:

What tree is in this photograph? [picture of a sycamore leaf]
Is this tumor cancerous? [picture of a tumor from an AI dataset] 
What word comes next? "Once upon a ..."

Notes/dialogue
“Artificial intelligence” is an enormous category, and no one sentence captures all of it. But this is the most useful starting point: modern AI learns patterns from examples and uses those patterns to make predictions.


## Next slide — How does a person learn?

A photograph of a parent and child looking at trees.

Three small labels:

Examples
Patterns
A new tree

Notes/dialogue

Imagine a father walking through the woods with his daughter. He points out an oak, a pine, and a maple. They do this again on another walk, and again the next year.

Eventually, she can recognize an oak she has never seen before. She has not merely memorized every individual tree. Somehow, she has learned useful patterns and can apply them to a new example.

That ability to perform well on a new example is called generalization. It is central to machine learning too.

Then establish the limit:

A computer does not learn exactly as a child does. A child has a body, relationships, intentions, and lived experience. This is an analogy about learning from examples—not a claim that a computer has a human mind.

## Next slide: How can we get computers to learn and make predictions?


Build the slide in three animation stages:

Scatterplot: square footage on the horizontal axis; sale price on the vertical axis. (no data)
add a standard dataset scatter plot on it. 
then add a badly placed line with long red error marks to each datapoint with equation y = ax + b displayed small but readable. 
make a gif with a schedule of a_n getting closer to the "best" a, and same with b_n, and when I play the gif we see the line walking to the best line. 

Small caption:

Adjust the model (y = ax+b) parameters (a,b) until its predictions better match the examples.


Notes/dialogue

Ask audience: Suppose I tell you that a house has 1,200 square feet. What might it sell for? What about 3,000 square feet?
You have a feel for it, b/c you've have experience. for a computer, data is the equivlanet of experience. 
A very simple computer model is to draw a line through past sales. For every house, we can measure the distance between the predicted price and the actual price. We then adjust the line to reduce those errors. (math optimization)
(I'll mention that square footage is relevant—but insufficient. You would also want its location, age, condition, and number of bedrooms.

## Next slide  — Training a machine-learning system
On the slide

A four-step cycle:

Collect examples
Choose a model (mathematical formula with parameters)
Adjust the parameters to reduce errors
Test it on new examples

At the center:

Training = learning useful patterns from data

Notes/dialogue

This is the basic recipe.

We collect examples. We choose a mathematical model capable of finding patterns. We adjust it—often millions or billions of times—to reduce its errors. Then we test it using examples it did not train on.

That final step is important. Memorizing yesterday’s answers is not enough. Like the child recognizing a new oak, the system must work on new cases.

Add:

The quality of the result depends on the data, the model, the goal we gave it, and how carefully we tested it.


## next slide: AI (Summarized) History

A simple four-part timeline:

Period	Examples
1990s–2000s	Spam filtering, fraud detection, recommendations
2010s	Image recognition, speech recognition, translation
Early 2020s	Generating text, images, audio, and code
Now	AI systems that use tools and take actions


Notes/dialogue

For decades, most AI systems were specialists. One identified spam. Another recommended movies. Another detected a pattern in a medical image.

More data, improved mathematics, and specialized computer chips produced major advances in image and speech recognition during the 2010s.

The current breakthrough is different because language is a general interface. We use language to discuss law, medicine, travel, history, recipes, and computer programs. A system that becomes broadly capable with language can assist with an enormous range of activities.

[Help me with Good news headlines and include them. something lie: 
AI is increasingly used in medical imaging e.g., better at identifying cancer than humans;
Include facial recognition as both a capability and a civil-liberties concern with news examples.
AI passes legal bar exam 
Navier Stokes equation headline]

As you can see with these last examples, modern AI is extremely capable. This is mostly driven by LLMs and technologies build around them. Let me give a quick introduction.


## Next Slide: Language Models
"Language Model" means the model predicts the next text. 


Sentence:

She opened the door and saw a ___

Possible next text:

dog
package
stranger
garden

Then show:

Text → small pieces called tokens → predicted next token → iterate

Notes/dialogue

Let’s do what the model does. “She opened the door and saw a…” What might come next?

These systems are trained on very large and diverse collections of text, code, and other data—but not literally everything, and not with perfect memory.

Take answers.

The model assigns possibilities to many possible continuations. It selects one, adds it to the text, and predicts again. Repeated very quickly, this produces paragraphs, poems, and computer programs.

A token is not always one word or one punctuation mark. It might be a whole word, part of a word, or punctuation. “Text broken into convenient pieces” is accurate enough for today.

## Next Slide — From text predictor to helpful assistant
On the slide

A three-stage diagram:

Broad pretraining
Learns patterns in language and knowledge

↓

Instruction and preference training
Learns to answer questions and follow directions

↓

Tools and safeguards
Search, calculation, coding, safety rules

An agent is an AI with tools and permission: Agent = model + goal + tools + permission to act

Possible tools:

Web browser
Calculator
Email
Computer code
Calendar
Files
Machinery
Notes/dialogue

A chatbot mainly produces an answer. An agent can pursue a goal through multiple steps.

Notes/dialogue

The first phase teaches the model broad patterns: grammar, writing styles, facts, code, and relationships among ideas.

A raw model is not automatically a good assistant. It then receives examples of instructions and desirable responses. Additional training teaches it to be more helpful, to reason through tasks, and to refuse certain harmful requests.

Modern AI products add still more software around the model: memory, web search, calculators, document access, and safety checks.

ChatGPT, Gemini, Claude, and Grok are products or services powered by models. They are not each simply “an LLM.”


## Next slide: LLM Agents and  Example use cases
The big change with AI starting in late 2010s was the ability of LLMs--Large Language models.
(Gemini, ChatGPT, GROK, ... are all examples of LLMs services.)

Let's do some examples: 
1. Create
2. Explain
3. Research

notes: 
Demonstration 1: Create

Gemini window: 
- "Write a warm, funny eight-line poem about Brookdale residents in south Kansas City learning to use AI. Include card games, Chiefs football, and one joke about technology. Keep it respectful."
- Rewrite it in iambic pentameter.
- Now rewrite it in the voice of Yosemite Sam

Demonstration 2: Explain
GROK: prepare a synthetic insurance or benefits notice:
Explain this notice in plain English. e is unclear.

Demonstration 3: Research

ChatGPT: I live at 119th and Lamar in Leawood Kansas. Find the official sample ballot for the election in Nov 2026. List each contest and link only to official election-authority pages. If you do not have enough information to determine my ballot, ask me for it rather than guessing.


## Next slide — What happens when you press Send?
On the slide

A simple diagram:

Underneath:

Your prompt usually leaves your device.

Notes/dialogue

In most consumer AI services, your question travels across the internet to a company’s data center. The service converts it into tokens, runs the model, may call a search engine or another tool, and returns the result.

Different products have different rules for storage, human review, and training. Therefore, do not assume that an AI conversation is private.

Practical rule: no private data into AI models! (or any cloud you don't trust)



## Next Slide: Tips

Be very specific with prompts. Have a conversation. Inspecting the result, and asking for revisions. Be very specific!


Verify consequential claims: AI Models make mistakes and "hallucinate" sometimes instead of saying they don't know or aren't certain when there is conflicting information. 

Treat voices and images as reproducible: real-seeming images and voices are AI now (deepfakes)

Never include confidential information into an AI model prompt:  
Do not paste passwords, Social Security numbers, bank details, confidential medical records, or another person’s private information into a consumer chatbot.

Never give broad permissions casually

## Agents = High potential &  risk

Left side: 

Include METR plot of agent capabilities based on length of human tasks they can complete and small caption. 

Color from green through yellow to red. 

Right side: Real Examples
- An email agent reportedly bulk-deleted hundreds of messages after losing track of its instruction to wait for approval.
- Mythos Preview is so good at coding it found and exploited vulnerabilities in well-used software
- OpenAI HuggingFace hack: AI agents break out of training and testing sandboxes to hack HuggingFace (AI infrastructure company)
- Navier Stokes Equation solution claimed by OpenAI in 88 hours. 


## Last slide: Worldly Issues
- is AI displacing jobs? 
- China and US are leading. Cultural influence and soverignity issues (other nations are influenced and dependent on US/China)
- Cybersecurity is undergoing a huge change
- Can we contain agents?