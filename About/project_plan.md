# Reflective Journal Analyzer

## Project Plan (Presentation Version)

This project helps users reflect on their day through journaling to improve mental health in a private, local-first setting.

---

### 0. Cover

- **Project Name:** Reflective Journal Analyzer  
- **Team:**  
  - Nino Sabella  
  - Evita Vardhani  
  - Rajan Puri  
- **Date:** Spring/Summer 2025

---

### 1. Problem Statement & Vision

**Pitch**  
> “Help people reflect on their day through journaling to improve their mental health in a private setting.”

**Why Now?**  
- There's a market gap for high-privacy, high-mental-health-value apps.

**Pain Points**  
- Users don’t reflect regularly (miss mood patterns)  
- Existing tools feel robotic  
- Lack of emotional understanding  
- Privacy concerns with cloud journaling

**Target Users**  
- Anyone looking to reflect on daily emotions  
- Privacy-conscious individuals  
- New journalers seeking guidance

**Success Criteria**  
- Easy daily journaling  
- Accurate sentiment analysis  
- Clear recurring theme detection  
- Human-like, relevant suggestions  
- Full local privacy by default

---

### 2. Scope

**Must-Have**  
- Daily prompt and journal input  
- Sentiment analysis  
- Mood summary with simple visualization  
- Local-first data storage  

**Nice-to-Have**  
- Recurring theme detection  
- Empathetic suggestions  
- Editable journal history  

**Stretch Goals**  
- End-to-end encrypted sync  
- Mood trend dashboard  
- Voice-to-text journaling  

**Out of Scope**  
- Real-time mental health diagnosis  
- Integration with 3rd-party apps  
- Social features

---

### 3. User Stories

- “I want to write a short journal entry every day, so I can track my thoughts and feelings.”  
- “It’d help to receive a mood summary after I write, so I can understand how I’ve been feeling.”  
- “It’s important for me to know what themes or topics reoccur in my life, so I can focus on and address them.”  
- “I’d like to receive useful suggestions based on what I’ve said, so I can improve my mental state.”  
- “I need to know the data stays on my device, so I feel safe writing in full honesty and vulnerability.”  

---

### 4. System Overview

**Frontend**  
- Prompts user daily  
- Journal entry input  
- Displays mood summary, suggestions, and themes  

**LLM-Powered Backend**  
- Sentiment analysis  
- Theme clustering  
- Empathetic responses  

**Storage Layer (Local-First)**  
- Saves journal entries and results on-device  
- (Optional) Encrypted backup  

**Data Flow**  
1. User opens app and submits entry  
2. Entry sent to LLM backend  
3. Returns:
   - Sentiment (e.g., “calm”, “stressed”)  
   - Key themes (e.g., “family”, “basketball”)  
   - Suggestion (e.g., “go for a walk”)  
4. Results shown in UI  
5. Data stored locally  

---

### 5. Project Timeline

| Date     | Milestone                                  | Owner         | Deliverable                                              |
|----------|---------------------------------------------|---------------|----------------------------------------------------------|
| May 15   | Finalize project idea & requirements        | Team          | Plan, tech stack, user stories, architecture             |
| May 22   | Research & test LLM tasks                   | Nino          | Hugging Face test scripts                                |
| May 29   | Set up local storage + basic UI             | Evita & Rajan | Journal form + local file or SQLite saving               |
| June 5   | Midterm presentation + demo                 | Team          | Slide deck + prototype                                   |
| June 19  | Integrate LLM backend                       | Nino          | API returning mood, themes, suggestions                  |
| June 26  | UI improvements + visualizations            | Rajan         | Charts/timeline for mood & themes                        |
| July 3   | (Stretch) Encrypted sync                    | Optional/Evita| Backup/sync setup                                        |
| July 10  | Bug fixing, UX polishing                    | Team          | Full user flow, error handling, save/load                |
| July 17  | Final Presentation + demo                   | Team          | Final slides, live demo, backup video                    |

---

### 6. Roles & Responsibilities

**Nino**  
- LLM Backend (sentiment, themes, suggestions)  
- API integration (FastAPI/Flask Blueprint)  

**Rajan**  
- Frontend (Flask, UI, forms, templates)  
- User flow and prompt interaction  

**Evita**  
- Local storage and data handling  
- Encrypted backup (stretch)  

**Shared**  
- Presentation and demo co-leads  

---

### 7. Risk Register

| Risk                                       | Probability | Impact | Mitigation Strategy                                                  |
|-------------------------------------------|-------------|--------|-----------------------------------------------------------------------|
| LLM outputs are low quality                | Medium      | High   | Test early, fine-tune prompts, fall back to rule-based logic         |
| Local storage fails                        | Low         | High   | Test regularly, version files, backup locally                        |
| Encrypted sync is too complex              | High        | Medium | Keep it optional                                                     |
| Frontend UI is hard to use                 | Medium      | Medium | Get early feedback, build simple UI first                            |

---

### 8. Evaluation & Demo Plan

**Success Metrics**  
- Users can write and see mood summaries  
- Sentiment matches tone  
- Recurring themes are correctly detected  
- Suggestions feel human  
- Data is saved & retrieved locally  
- App works offline  

**Demo Script**  
1. Open app and introduce it  
2. Enter a sample journal entry  
3. Show:
   - Mood summary (e.g., “anger”, “fear”)  
   - Suggestion (e.g., “try deep breathing”)  
   - Themes (e.g., “work”, “mom”)  
4. Load past entries  
5. (Optional) Show theme clustering / mood trends  
6. Highlight privacy, personalization, and mental health benefits  

**Backup Plan**  
- Record full demo video (Week 9)  
- Show complete app flow offline  
- Store video locally for presentation day  

---
