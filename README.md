## Interview questions

### Suggested Timing (45-60 minutes)

- Section 0: 10-15 min
- Sections 1-4: 5-7 min each
- Section 5: 10-15 min
- Leave 5 min for candidate questions

0. To start
    - Tell about yourself
    - Tell about a project you've done
    - Why did you choose python as your programming language?


1. Python
    - What is the difference between a list and a tuple?
    - What is a function, class?
    - What's the difference between a class and an object?
    - What is self?


2. API
    - What are REST and API?
    - What HTTP methods do you know?
    - What are status codes?
    - How can we prevent the server from working with invalid data sent by the client?


3. Database
    - What are migrations?
    - What is a JOIN? What's the difference between INNER and OUTER?
    - How can you speed up database queries when there is a lot of data?


4. Workspace
    - What is venv? Why is it important to use a virtual environment?
    - What is a branch in git?
    - What is a merge conflict and how do you resolve it?
    - What is a Dockerfile? What is the main purpose of a Dockerfile?


5. Advanced
    - What happens in the browser when you type a URL and hit enter?
    - If you were building an API, how would you control who can access it?
    - Have you heard of unit testing? Can you explain why it might be useful?
    - What is the difference between synchronous and asynchronous code? Have you used async/await in Python?


6. Problem-Solving Approach
    - Tell me about a technical challenge you faced and how you solved it.
    - How do you approach learning a new technology or framework?

<hr>


## Livecoding

### Suggested Timing (60-75 minutes)

#### Part 1: Debugging & Logic (15-20 min)
- Clone repository and open tasks.py
- Complete debugging and UserActionHistory tasks

#### Part 2: Backend Setup (10-15 min)  
- Install requirements
- Add missing Category model
- Run migrations and seed data

#### Part 3: API Implementation (25-30 min)
- Complete GET /products endpoint
- Complete POST /orders endpoint
- Test via Swagger

#### Part 4: Discussion (10 min)
- Walk through solutions
- Discuss tradeoffs and alternatives

<hr>

## What We're Looking For:

### Debugging
- [ ] find_user_by_email works correctly
- [ ] UserActionHistory methods implement spec
- [ ] Edge cases handled (empty inputs, etc.)

### Backend Tasks
- [ ] Category model has id, name and relationship
- [ ] GET /products returns correct data with JOIN
- [ ] Includes pagination (offset/limit)
- [ ] POST /orders validates stock availability
- [ ] Uses database transaction
- [ ] Proper error responses
