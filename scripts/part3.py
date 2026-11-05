from authoring import make,Q
LESSONS=[]
LESSONS.append(make(
16,'Professional Emails','Деловая электронная переписка','clear professional emails',
'''subject line | тема письма | The short heading that tells readers the email\'s purpose. | Use a specific subject line for your request.
recipient | получатель | The person an email is sent to. | Check the recipient before sending the file.
attachment | вложение | A file sent with a message. | The revised schedule is in the attachment.
concise | краткий и содержательный | Short and clear without unnecessary detail. | A concise email is easier to act on.
request | запрос; просьба | A polite statement asking someone to do something. | The email includes a request for confirmation.
appropriate tone | подходящий тон | A style of language suitable for the situation. | Use an appropriate tone with new partners.
proofread | вычитать | To check writing for mistakes before sending. | Always proofread names and dates.
closing | заключительная формула | The final words of a letter or email. | Kind regards is a common professional closing.
thread | цепочка переписки | A sequence of messages about one subject. | Keep the relevant discussion in one email thread.
action required | необходимое действие | What the reader needs to do next. | Make the action required clear near the end.''',
'''I am writing to enquire about… | Пишу, чтобы уточнить…
Could you please confirm…? | Не могли бы вы подтвердить…?
Please find the attached document. | Документ приложен к письму.
For your reference, I have included… | Для справки я включил(а)…
I would appreciate your response by… | Буду признателен(на) за ответ до…
Kind regards, | С уважением,''',
'A request that is easy to answer',
'''An Academic Support officer needs a partner university to confirm the names of two visiting lecturers. The original draft email is long, contains several unrelated topics and does not specify when the information is needed. Even polite messages can be difficult to answer if the reader cannot identify the request. The officer revises the draft to make its purpose visible immediately.
The new subject line says “Visiting lecturers — name confirmation for 18 November”. The opening sentence states why the officer is writing. A short middle paragraph gives the relevant context: the names will appear in a workshop schedule, so spelling matters. The final sentence asks for confirmation by a specific date and invites questions. The officer checks that the deadline is reasonable and that any necessary document is attached.
Professional email style does not require unusually formal vocabulary. “Could you please confirm…” is often clearer than a complicated phrase about “your esteemed institution”. The officer uses the recipient\'s preferred title when known, but avoids guessing. They also proofread names, dates, links and the attachment. The result is an email that helps the reader take action in under a minute. Good correspondence respects the recipient\'s time and creates a useful written record of the agreed next step.''',
'''Partner | I received your message, but I\'m not sure what you need from us.
Officer | Thank you for letting me know. I should have made the request clearer.
Partner | Are you asking us to approve the whole workshop programme?
Officer | No, just to confirm the spelling of the two visiting lecturers' names.
Partner | Understood. When do you need the confirmation?
Officer | By 14 November if possible, so we can finalise the printed schedule.
Partner | Could you send the draft list?
Officer | Certainly. I\'ll reply with the list attached and a specific subject line.''',
('Polite email requests','Вежливые просьбы в письмах','Use a clear purpose, context and action. “Could you please…?” and “I would appreciate…” work well; avoid inflated formality.','I am writing to confirm the schedule.;Could you please check the two names?;I would appreciate a reply by Friday.','Avoid vague subject lines such as “Important!!!” without context.',Q('Choose the clearest polite request.','Could you please confirm the two names by Friday?','Dear institution, do the necessary.','Need this now immediately.','Specific action and deadline improve clarity.')),
[Q('What makes the revised email easier to answer?','It has a clear subject, context and requested action.','It uses much longer sentences.','It removes all deadlines.','The revised message makes the reader’s task obvious.'),Q('Why are the names being checked?','They will appear in a workshop schedule.','They are required for a grading appeal.','They are needed for a room booking deposit.','Accurate spelling matters for the printed programme.')],
[Q('What does the officer actually need confirmed?','The spelling of two lecturers’ names.','Approval of the entire workshop.','A new university partnership.','The officer explicitly narrows the request.'),Q('When is confirmation requested?','By 14 November.','By 18 November.','After the workshop.','The officer gives a working deadline before printing.')],
'Edit an unclear email: add a specific subject, one request, relevant context and a realistic deadline.',
'Explain to a new colleague how you would write an email requesting programme information from a partner.',
'I would use a specific subject line, explain the reason for the message, and ask one clear question. I would give any relevant deadline and check attachments, names and dates before sending. I would end with a polite closing.',
'Write a 90–120-word email asking an international partner to confirm visiting lecturers’ names for a workshop.',
'Subject: Lecturer name confirmation — Workshop on 18 November\nDear Dr Chen, We are preparing the workshop schedule for 18 November and would appreciate your help confirming the spelling and titles of the two visiting lecturers. I have attached the current draft list for your review. Could you please send any corrections by 14 November so that we can finalise the programme? Please let me know if anything is unclear. Kind regards, Alex',
('I am writing for ask about the timetable.','I am writing to ask about the timetable.','Use to + infinitive to express purpose.'),
Q('Your partner asks what action is needed in a long email. How should you improve it?','Send one clear request with context and a deadline.','Add more unrelated background.','Use only an urgent emoji.','Writing should make the next action obvious.')))
LESSONS.append(make(
17,'Email Follow-ups & Diplomatic Writing','Напоминания и дипломатичная переписка','follow-up emails, reminders and delays',
'''follow-up | последующее обращение | A message after earlier contact. | I sent a follow-up about the pending document.
pending | ожидающий решения | Not yet completed or decided. | The confirmation is still pending.
gentle reminder | вежливое напоминание | A courteous message about an unanswered request. | A gentle reminder may be helpful before the deadline.
delay | задержка | Extra time beyond what was expected. | The team explained the reason for the delay.
appreciate | быть признательным | To value someone\'s help or action. | We appreciate your cooperation.
status enquiry | запрос статуса | A request for progress information. | The partner sent a status enquiry yesterday.
diplomatic | тактичный | Careful and respectful when discussing sensitive matters. | Use diplomatic wording to address the disagreement.
acknowledge receipt | подтвердить получение | To confirm that a message or document arrived. | Please acknowledge receipt of the revised file.
inconvenience | неудобство | Trouble caused to another person. | We apologise for any inconvenience.
revised timeframe | обновлённый срок | A changed estimate or schedule for a task. | The team will share a revised timeframe when available.''',
'''I am following up on my previous message. | Возвращаюсь к своему предыдущему письму.
I just wanted to check whether… | Хотел(а) уточнить, удалось ли…
We would appreciate an update when possible. | Будем признательны за обновление, когда будет возможность.
Thank you for your patience. | Спасибо за терпение.
I apologise for the inconvenience. | Приношу извинения за неудобства.
Please let me know if you require further information. | Сообщите, если нужна дополнительная информация.''',
'Following up without sounding demanding',
'''A partner university has not replied to a request for updated course descriptions. The Academic Support officer sent the original email six working days ago, and the local review meeting is approaching. A follow-up is appropriate, but the officer wants to avoid sounding accusatory. They begin by checking whether the previous message reached the right contact and whether the deadline was clearly stated.
The new email briefly references the earlier request and explains why the documents are needed. Rather than writing “You have failed to respond,” the officer asks whether an update is available and offers to provide additional information. They include a suggested date for a response, but acknowledge that the partner may need more time. This approach keeps the request actionable while preserving a cooperative relationship.
Later, the partner responds that a staff change has delayed the documents. The officer thanks them for the update and asks whether a revised timeframe can be shared. It would be unwise to announce that the materials will arrive tomorrow when the partner has not confirmed that. The officer can instead inform the local team that the documents remain pending. Diplomatic writing is not about hiding facts. It is about stating facts accurately, allowing the other person to respond and avoiding unnecessary blame. This matters in international partnerships where tone can be interpreted differently across institutions.''',
'''Officer | Hello, I\'m following up on our request for the updated module descriptions.
Partner | Thanks for checking in. We\'ve had a staffing change, so the documents are delayed.
Officer | I appreciate the update. Do you have a revised timeframe in mind?
Partner | We hope to send them next week, but I can\'t confirm a date yet.
Officer | Understood. I\'ll tell our team that the documents are still pending.
Partner | Is there a particular section you need first?
Officer | The learning outcomes would be especially helpful. Could you share that section when available?
Partner | Yes, I\'ll see what we can provide.''',
('Softening and hedging','Дипломатичные формулировки','Use would, could, just wanted to and when possible to soften requests without obscuring the action. Avoid false certainty about pending work.','I was wondering if there is an update.;Would it be possible to share a timeframe?;We expect an update, but no date is confirmed.','“Just wanted to check” is polite, but do not overuse apologies or make the purpose unclear.',Q('Which follow-up is professional and clear?','Would it be possible to share an updated timeframe?','You never reply; send everything immediately.','This request is urgent because I say so.','The wording invites a useful answer without blame.')),
[Q('Why is a follow-up reasonable in the example?','The request is unanswered and a review meeting is approaching.','The partner has definitely refused to help.','The materials are no longer needed.','The officer has a clear operational reason to check.'),Q('What should the officer tell the local team?','The documents remain pending without a confirmed date.','The documents will certainly arrive tomorrow.','The partner has cancelled all collaboration.','Report known status rather than assumptions.')],
[Q('Why are the documents delayed?','A staffing change.','A cancelled student exam.','A weather emergency.','The partner explicitly mentions staffing changes.'),Q('Which section would help first?','Learning outcomes.','The campus café menu.','The lecturers’ holiday schedule.','The officer prioritises the learning outcomes section.')],
'Write a polite reminder that references the original request, gives context and asks for a realistic update.',
'A partner has missed a suggested date. Request a status update without accusing anyone or promising a new deadline.',
'I am following up on our earlier request for the module descriptions. We need them for a forthcoming review. Could you let us know whether an updated timeframe is available? Please tell us if any additional information would help.',
'Draft a diplomatic follow-up to a partner who has not replied about a document request. Include an optional response date.',
'Subject: Follow-up — Updated module descriptions\nDear Colleagues, I hope you are well. I am following up on our message from last week concerning the updated module descriptions. Our internal review is approaching, and we would appreciate any update you can share. If possible, could you let us know the current status by Thursday? Please tell us if you need any further details from our side. Kind regards, Alex',
('I look forward to hear from you.','I look forward to hearing from you.','Look forward to is followed by a noun or -ing form.'),
Q('A partner cannot confirm a delivery date. What should you report internally?','The item is pending, and a revised date is not yet confirmed.','It will definitely arrive tomorrow.','The partner has refused all support.','Report uncertainty accurately rather than inventing dates.')))
LESSONS.append(make(
18,'Online Meetings','Онлайн-встречи','online meeting participation and technical issues',
'''join a call | присоединиться к звонку | To enter an online meeting. | Please join the call five minutes early.
agenda | повестка | A list of topics planned for discussion. | The agenda includes three academic updates.
audio issue | проблема со звуком | A problem with hearing or sending sound. | We have an audio issue on one participant\'s connection.
screen sharing | демонстрация экрана | Showing your screen to other participants. | Screen sharing will help explain the document.
mute | выключить микрофон | To prevent your microphone from transmitting sound. | Please mute your microphone when not speaking.
connection | соединение | The link allowing online communication. | The connection became unstable during the presentation.
chair the meeting | вести встречу | To lead the order and discussion. | The programme director will chair the meeting.
recap | подвести итог | To briefly repeat the key points. | Let\'s recap the agreed steps before leaving.
meeting link | ссылка на встречу | The address used to join an online session. | I will resend the meeting link.
minutes | протокол встречи | A written record of key discussion and decisions. | We will circulate the minutes tomorrow.''',
'''Can everyone hear me clearly? | Все меня хорошо слышат?
You\'re on mute at the moment. | У вас сейчас выключен микрофон.
Could you share your screen, please? | Не могли бы вы показать экран?
The connection seems unstable. | Похоже, связь нестабильна.
Shall we move to the next agenda item? | Перейдём к следующему пункту повестки?
Before we finish, let me recap the action points. | Перед завершением подведу итог задач.''',
'A hybrid meeting with an unexpected problem',
'''An Academic Support officer joins an online coordination meeting with colleagues at a partner university. Some participants are in a campus meeting room and others are joining remotely. Before the discussion begins, the chair checks whether everyone can hear and see the shared screen. This simple step prevents important information from being missed by people who are not physically present.
During the first agenda item, a remote lecturer\'s microphone stops working. Instead of ignoring the lecturer, the officer suggests using the meeting chat temporarily and offers to repeat the key question. When the connection improves, the lecturer can rejoin the conversation. The team also realises that an old version of the timetable is being shared. The officer clearly identifies the revised document and confirms that participants are looking at the same version.
At the end, the chair asks the officer to recap the agreed action points. The officer distinguishes a decision from a suggestion: the new workshop date is confirmed, but the room still needs checking. This distinction should appear in the meeting notes and follow-up email. Successful online communication combines clear language with inclusive meeting habits. Participants need opportunities to ask questions, repair technical problems and confirm what has actually been agreed. Speaking clearly is more important than speaking quickly.''',
'''Chair | Welcome, everyone. Can you all hear me clearly?
Lecturer | I think my microphone is not working.
Officer | We can see your messages in the chat. Would you like me to read your question aloud?
Lecturer | Yes, please. Is the updated timetable on screen?
Officer | Not yet. We are viewing the previous version. I\'ll share the revised file now.
Chair | Thank you. Have we agreed on the workshop date?
Officer | Yes, the date is confirmed, but the room is still pending.
Chair | Good. Please include that distinction in the meeting notes.''',
('Present Continuous for live situations','Настоящее длительное время','Use Present Continuous for actions in progress during a call: “We are viewing the previous version.” Use Present Simple for routine procedures.','We are sharing the updated timetable now.;The lecturer is typing in the chat.;We normally send minutes after meetings.','Avoid confusing a live action with a general habit.',Q('Which sentence describes what is happening right now?','We are sharing the updated document.','We sharing the updated document.','We share yesterday the updated document.','Present Continuous describes an action in progress.')),
[Q('What is confirmed at the end of the meeting?','The workshop date but not the room.','Both date and room.','Neither topic has been discussed.','The recap distinguishes confirmed and pending items.'),Q('How does the team include the lecturer with audio trouble?','By using the chat and reading their question aloud.','By ending the call immediately.','By ignoring their contribution.','Inclusive online participation provides alternative channels.')],
[Q('What is wrong with the file first shown on screen?','It is the previous version.','It is a confidential student transcript.','It has no title.','The officer notices an outdated timetable.'),Q('What should be recorded in the notes?','Date confirmed; room pending.','Everything confirmed.','No follow-up required.','The chair asks for accurate status distinctions.')],
'Join a hybrid meeting, handle a microphone problem and recap confirmed versus pending decisions.',
'You are supporting a virtual academic meeting. Explain a technical problem and guide participants to the correct document.',
'It looks as though the wrong version of the timetable is currently on screen. I will share the revised file now. If anyone has audio difficulties, please use the chat, and I can read your question aloud. Before we finish, I will recap the agreed actions.',
'Write a five-sentence follow-up after an online meeting: one decision, one pending item, an owner and a next step.',
'Dear Colleagues, Thank you for joining today’s coordination meeting. We confirmed the workshop date of 18 November. The room allocation remains pending and will be checked by the scheduling team. I will circulate the revised timetable once that detail is confirmed. Please let me know if I have missed any action points. Kind regards, Alex',
('We sharing the screen now.','We are sharing the screen now.','Present Continuous requires be + verb-ing.'),
Q('A remote lecturer cannot speak. What should you do?','Invite a written question and include it in the discussion.','Continue as though the lecturer is absent.','Announce that their opinion is no longer needed.','Accessibility and participation are important in hybrid meetings.')))
LESSONS.append(make(
19,'Participating in Discussions','Участие в профессиональных обсуждениях','agreeing, disagreeing and building on ideas',
'''contribute | вносить вклад | To add an idea or information to a discussion. | Please contribute your perspective on registration.
perspective | точка зрения | A way of understanding an issue. | The student services team has another perspective.
raise a point | поднять вопрос | To introduce an idea for discussion. | May I raise a point about the deadline?
agree in principle | соглашаться в целом | To accept the general idea while details remain open. | I agree in principle, but we need to check capacity.
concern | сомнение; опасение | A question about a risk or possible problem. | I have one concern about the timetable.
build on | развить идею | To add detail to someone else\'s suggestion. | I would like to build on Maria\'s proposal.
alternative | альтернатива | Another possible option. | Could we consider an alternative schedule?
consensus | общее согласие | Broad agreement among the people involved. | The group reached consensus on the next step.
trade-off | компромисс между выгодами и затратами | A balance where improving one thing may limit another. | A later deadline involves a trade-off.
clarify a point | уточнить тезис | To ask for or give a clearer explanation. | Could I clarify one point before we decide?''',
'''I\'d like to add something here. | Я хотел(а) бы кое-что добавить.
I agree with the main idea, but… | Я согласен(на) с основной идеей, но…
Could I raise one concern? | Можно высказать одно опасение?
Building on that point… | Развивая эту мысль…
Would an alternative approach be possible? | Возможен ли альтернативный подход?
It seems we agree on the next step. | Похоже, мы согласовали следующий шаг.''',
'A discussion about orientation support',
'''Several departments are planning orientation activities for international students. The programme coordinator suggests one long information session covering registration, digital systems and academic rules. The Academic Support officer agrees that students need all three topics, but worries that a single long session may be difficult to follow. Rather than rejecting the proposal directly, they say, “I agree with the aim, but could we consider two shorter sessions?”
The IT colleague supports the idea and suggests a live demonstration of the learning platform. Another team member raises a concern: two sessions may be harder to schedule. The group compares the options. A single meeting is administratively simple, while shorter meetings may give students more opportunities to ask questions. The best choice depends on available staff time and the needs of the students.
The officer summarises what the group appears to agree on: registration information is essential, practical demonstrations are valuable, and the final schedule needs checking. No one has yet approved a specific format. This is an important distinction between consensus on principles and a final decision. Constructive participation means listening, connecting your suggestions to shared goals and acknowledging trade-offs. Polite disagreement helps a group improve a plan without turning the conversation into a personal conflict.''',
'''Coordinator | I suggest we cover all orientation topics in a single three-hour session.
Officer | I agree that all topics are important, but could we consider two shorter sessions?
IT Colleague | Building on that idea, we could include a live platform demonstration.
Coordinator | My concern is that two sessions may be harder to schedule.
Officer | That\'s a fair point. Could we compare the available time slots before deciding?
IT Colleague | We could send an online guide before the sessions as well.
Coordinator | It seems we agree on the content, but not yet on the format.
Officer | Exactly. I can summarise the options and ask scheduling to check availability.''',
('Diplomatic agreement and disagreement','Согласие и несогласие','Acknowledge a useful point before adding a concern. “I agree that…, but…” and “Could we consider…?” are collaborative rather than confrontational.','I agree with the aim, but timing could be difficult.;That is a fair point.;Could we consider two shorter sessions?','Avoid “You are wrong” when discussing a shared plan.',Q('Which reply expresses constructive disagreement?','I agree with the aim, but could we consider another format?','Your plan makes no sense.','I refuse to discuss the issue.','Acknowledge the shared goal before suggesting an alternative.')),
[Q('What is the officer’s main concern?','A single long session may overload students.','Registration information is unnecessary.','IT should not attend.','The officer proposes a format change for learning reasons.'),Q('What is not yet decided?','The final format and schedule.','Whether registration is important.','Whether students should be helped.','The group agrees on content but not format.')],
[Q('What alternative does the officer propose?','Two shorter sessions.','Cancel orientation.','One six-hour session.','The officer’s proposal is explicit.'),Q('What will be checked before a decision?','Available time slots.','Students’ favourite colours.','The price of the campus café.','The officer suggests comparing scheduling options.')],
'Contribute to an academic meeting with one opinion, one respectful concern and one workable alternative.',
'A coordinator proposes a very long orientation session. Express a polite concern and propose a practical alternative.',
'I agree that the students need all the information, but one long session might be difficult to follow. Could we consider two shorter sessions and an online guide? We should check staff availability before making a final decision.',
'Write three short discussion contributions: one agreement, one concern, and one alternative proposal.',
'I agree that registration guidance should be included. My concern is that a three-hour session may be difficult for new students to follow. Could we consider two shorter workshops and provide written instructions in advance?',
('I agree with to your proposal.','I agree with your proposal.','Agree with a person or proposal; do not insert to in this construction.'),
Q('A colleague proposes a solution with a clear drawback. What is best?','Recognise the benefit and raise the drawback constructively.','Attack the colleague personally.','Agree silently despite serious concerns.','Professional discussion considers trade-offs respectfully.')))
LESSONS.append(make(
20,'Presenting Academic Information','Презентация академической информации','clear explanations and mini-presentations',
'''overview | обзор | A brief introduction to the main information. | I\'ll begin with an overview of the programme.
outline | кратко изложить | To describe the main parts without full detail. | Let me outline the registration process.
highlight | подчеркнуть | To draw attention to something important. | I would like to highlight the key deadline.
transition | переход | A phrase connecting one part of a presentation to another. | Use a clear transition between topics.
visual aid | наглядный материал | An image, table or slide supporting an explanation. | The flowchart is a useful visual aid.
key takeaway | главный вывод | The most important point for the audience to remember. | The key takeaway is to check the official portal.
summarise | подытожить | To restate key information briefly. | I will summarise the steps at the end.
audience | аудитория | The people listening to a presentation. | Adapt the explanation to the audience.
sequence | последовательность | An ordered series of steps or events. | The slide shows the sequence of approvals.
question period | время для вопросов | A scheduled opportunity to ask questions. | We have five minutes for the question period.''',
'''Let me give you a brief overview. | Позвольте дать краткий обзор.
There are three main points to cover. | Есть три основных момента.
First, I\'d like to highlight… | Сначала хочу выделить…
Moving on to the next point… | Переходя к следующему вопросу…
The key takeaway is… | Главный вывод заключается в том, что…
I\'d be happy to take questions. | Я с удовольствием отвечу на вопросы.''',
'A five-minute briefing about academic requests',
'''The Academic Support officer has been asked to give a five-minute briefing to new international staff. The topic is the process for handling student document requests. Although the officer knows the procedure well, the audience may not understand local department names or abbreviations. The officer therefore prepares a simple three-part structure: where a request begins, how it is reviewed, and how the student receives an update.
The first slide shows the official submission channel. The second explains the difference between checking a form for completeness and approving the underlying request. The third gives the correct contact routes for questions. Rather than filling the screen with paragraphs, the officer uses a short process diagram and speaks in complete but manageable sentences. They avoid promising that every request has the same processing time.
Near the end, the officer summarises the key takeaway: students should use the official process, while support staff guide and track requests within their authority. The officer then invites questions and checks understanding. A visitor asks about exceptions. Instead of delivering an uncertain answer, the officer explains that exceptions are reviewed by authorised teams under published policy. A strong presentation uses accurate content, clear organisation and a supportive tone. It is not necessary to use elaborate vocabulary to sound professional.''',
'''Chair | Alex, could you give us a quick overview of the document request workflow?
Officer | Of course. There are three main stages: submission, verification and follow-up.
Visitor | Does Academic Support make the final decision?
Officer | Not in every case. We check completeness and coordinate, while authorised teams decide where required.
Chair | What is the key message for new staff?
Officer | Direct students to the official channel and explain which team owns the next step.
Visitor | And what about exceptions?
Officer | Those depend on the published policy and should be reviewed by the authorised team.''',
('Signposting a presentation','Связки для структурированной речи','Use first, next, moving on and finally to guide listeners. State the main message at the beginning and repeat it briefly at the end.','First, I will explain the submission stage.;Moving on to verification…;To summarise, use the official request channel.','Avoid reading long slide text word for word.',Q('Which phrase is suitable for changing topics?','Moving on to the next point…','Everything I say is obviously clear.','I done next part.','Signposting helps listeners follow the structure.')),
[Q('What are the briefing’s three parts?','Submission, verification and follow-up.','Admission, graduation and housing.','Teaching, research and sports.','The presentation follows the request process.'),Q('What visual approach does the officer choose?','A simple process diagram, not dense paragraphs.','Slides full of unrelated text.','No explanation of department roles.','Visuals should support, not replace, clear speech.')],
[Q('Does Academic Support approve every request?','No; authorised teams make decisions where required.','Yes, regardless of policy.','Only visitors can approve them.','The officer explains departmental limits.'),Q('What should new staff tell students?','Use the official channel and identify the right next step.','Email private documents to anyone.','Wait indefinitely without information.','The key message is practical guidance.')],
'Present a three-step academic request workflow in two minutes, including one limitation and an invitation to questions.',
'Give a short briefing to visiting staff about how document requests are processed.',
'Let me give you a brief overview. First, students submit requests through the official channel. Next, the responsible team verifies the information. Finally, support staff help coordinate follow-up. The key takeaway is that guidance and approval are different responsibilities. I would be happy to answer questions.',
'Draft a 100-word script for one slide that explains a three-stage document request process.',
'Our document request process has three stages. First, the student completes the form through the official portal. Second, the responsible team checks the information and determines whether any additional documents are needed. Third, the student receives an update through the approved channel. Academic Support guides the process, but it does not make every academic decision. Please use the contact details on this slide if you need help identifying the correct team.',
('Let me to outline the three steps.','Let me outline the three steps.','Let + object is followed by the base verb without to.'),
Q('A listener asks a question you cannot verify during your presentation. What is best?','State that you will check the current policy and follow up.','Invent an answer confidently.','Avoid any further questions.','Credible presenters separate known facts from uncertainties.')))
LESSONS.append(make(
21,'International Partnerships','Международное академическое сотрудничество','partner university coordination',
'''partner institution | партнёрский университет | An organisation collaborating with another institution. | We are coordinating with a partner institution overseas.
academic collaboration | академическое сотрудничество | Joint work related to teaching or scholarship. | The programme supports academic collaboration.
exchange arrangement | соглашение об обмене | A structured plan for participants to study or work elsewhere. | Exchange arrangements require formal confirmation.
contact person | контактное лицо | The person responsible for communication. | Please confirm your contact person for this programme.
coordinate logistics | координировать организационные вопросы | To organise practical details for an activity. | We coordinate logistics for visiting lecturers.
memorandum of understanding | меморандум о взаимопонимании | A document recording a framework for cooperation; its legal effect varies. | The institutions are discussing a memorandum of understanding.
reciprocal | взаимный | Involving corresponding actions on both sides. | The exchange includes reciprocal visits.
agreed scope | согласованный объём | The activities and responsibilities that participants have accepted. | Let\'s stay within the agreed scope of support.
point of escalation | контакт для эскалации | A person or channel for issues that need higher-level attention. | The partnership office is the point of escalation.
liaison | координатор взаимодействия | A person who helps communication between groups. | The liaison keeps both teams informed.''',
'''Could you confirm the relevant contact person? | Не могли бы вы подтвердить контактное лицо?
Our role is to coordinate practical arrangements. | Наша роль — координировать организационные вопросы.
This requires formal institutional approval. | Это требует официального согласования университета.
Let\'s clarify the agreed scope of work. | Давайте уточним согласованный объём работы.
I will liaise with the partnerships office. | Я свяжусь с отделом партнёрств.
We appreciate the opportunity to collaborate. | Мы ценим возможность сотрудничать.''',
'Helping a partner without changing the agreement',
'''A partner university plans to send two visiting lecturers for a short academic workshop. The institutions already have a general cooperation framework, but the proposed visit still needs practical arrangements. Academic Support can help with room booking, an outline schedule and information about campus access. A separate partnerships office manages formal agreements and the scope of institutional commitments.
During a coordination call, the partner asks whether the workshop can be extended into a credit-bearing summer programme. This would be a significant change. The officer does not reject the idea as impossible, but also does not approve it. They explain that any formal academic arrangement requires discussion with authorised departments and, depending on the institutions, an appropriate agreement or amendment.
The officer brings the conversation back to confirmed tasks. The lecturers' arrival dates are provisional; the workshop topics have been agreed in principle; and the host department still needs to nominate a contact person. A useful follow-up email separates agreed facts, open questions and named responsibilities. International partnerships work best when different offices contribute within their expertise. Support staff are valuable because they create reliable communication and organise details, not because they can commit an entire university to new academic obligations. Clarity about scope protects the relationship.''',
'''Partner | We would like to confirm arrangements for the two visiting lecturers.
Officer | We can help coordinate the workshop schedule, campus access and room information.
Partner | Could we turn the visit into a credit-bearing summer programme?
Officer | That would require formal academic discussion and the appropriate institutional approval.
Partner | Who should be involved in that discussion?
Officer | I can connect you with the partnerships office and the relevant academic lead.
Partner | For now, shall we confirm the workshop dates?
Officer | Yes. I\'ll send a summary of what is agreed and what remains provisional.''',
('Would, could and require','Тактичные предложения и обязательные согласования','Could and would are useful for collaborative suggestions. Require expresses an actual formal condition. Keep provisional details separate from approved commitments.','Could we confirm the dates first?;We would be happy to coordinate logistics.;A new programme would require formal approval.','Avoid saying “We have approved this arrangement” without institutional authority.',Q('Which reply respects decision boundaries?','A new academic programme would require formal approval.','I can approve any new degree programme now.','Formal agreements are never necessary.','Changing a programme is not a routine logistical decision.')),
[Q('What can Academic Support coordinate directly in this example?','Workshop scheduling and practical logistics.','Legally binding new degree programmes.','All institutional partnership decisions.','The officer’s role is coordination, not authorisation.'),Q('Which details remain provisional?','The lecturers’ arrival dates.','The entire programme is already accredited.','The campus no longer exists.','The reading explicitly marks arrival dates as provisional.')],
[Q('Who should discuss a credit-bearing summer programme?','Authorised partnerships and academic teams.','Only the support officer.','Any visitor at the meeting.','Formal scope changes need institutional review.'),Q('What will the officer send after the call?','A summary of agreed and provisional items.','An unconditional approval letter.','A revised degree certificate.','The follow-up separates confirmed from pending details.')],
'Coordinate a partner visit and correctly refer a proposed expansion of academic scope for formal review.',
'A visiting coordinator asks you to approve a new academic programme during a logistics call. Respond helpfully without overstepping.',
'The workshop arrangements are within our coordination role, and I can help with the schedule and access information. A new credit-bearing programme would need formal academic and institutional approval. I can introduce you to the appropriate teams to discuss it.',
'Draft a partner follow-up email with two confirmed actions and two provisional items.',
'Dear Colleagues, Thank you for today’s coordination call. We agreed that Academic Support will prepare the draft workshop timetable and share campus access guidance. The lecturers’ arrival times and the host contact person remain to be confirmed. We will refer the proposed summer programme to the relevant partnerships and academic teams for separate consideration. We look forward to continuing our collaboration. Kind regards, Alex',
('This change require formal approval.','This change requires formal approval.','A singular subject in Present Simple takes -s.'),
Q('The partner suggests expanding a workshop into a degree-bearing activity. What do you say?','This needs academic and institutional approval; I can connect you with the right team.','I accept on behalf of the university.','Ignore the proposal and end the call.','Support staff should facilitate the correct review channel.')))
LESSONS.append(make(
22,'Cross-cultural Communication','Межкультурное профессиональное общение','culturally sensitive communication',
'''assumption | предположение | Something accepted without checking. | Avoid assumptions about communication preferences.
interpretation | трактовка | The meaning someone gives to a message. | The phrase caused different interpretations.
direct | прямой | Expressing a point clearly with little indirect wording. | Some teams prefer direct feedback.
indirect | косвенный | Expressing a point more gently or implicitly. | An indirect request may still contain an important action.
respectful | уважительный | Showing consideration for other people. | Use respectful language even when you disagree.
communication preference | предпочтение в общении | A person\'s preferred way of exchanging information. | Ask about communication preferences rather than guessing.
confirm expectations | уточнить ожидания | To check what each person believes will happen. | Confirm expectations before the project begins.
misinterpret | неправильно понять | To understand a message in the wrong way. | A short email can be easy to misinterpret.
cultural sensitivity | межкультурная чуткость | Awareness that experiences and norms differ across people. | Cultural sensitivity includes listening and avoiding stereotypes.
shared understanding | общее понимание | Agreement on what a message or plan means. | We ended with a shared understanding of the deadline.''',
'''Could you tell me how your team usually handles this? | Как ваша команда обычно решает этот вопрос?
I want to make sure we\'re aligned. | Хочу убедиться, что мы одинаково понимаем ситуацию.
Would you prefer a brief call or an email? | Вам удобнее короткий звонок или письмо?
I may have misunderstood your point. | Возможно, я неправильно понял(а) вашу мысль.
Thank you for explaining your perspective. | Спасибо, что объяснили вашу точку зрения.
Let\'s confirm our shared understanding. | Давайте уточним наше общее понимание.''',
'When a polite phrase has different meanings',
'''Two university teams are coordinating a joint webinar. During a call, one colleague says, “We could perhaps look at Friday.” The other team interprets the phrase as an agreed date and sends invitations immediately. The first colleague, however, meant that Friday was only a possibility. Neither person intended to mislead the other; they simply understood the level of commitment differently.
The Academic Support officer notices the misunderstanding and suggests confirming the details explicitly. They ask whether Friday is a proposed option or a final decision. Both teams agree that the date remains provisional until the speaker and technical team confirm availability. The officer then puts this distinction in writing, using the words “proposed” and “confirmed” rather than relying on the tone of the original phrase.
People sometimes describe cultures as always direct or always indirect. Such stereotypes can obscure individual preferences, institutional practices and the immediate situation. A safer approach is to ask, listen and confirm expectations. Different colleagues may have different habits even within the same university. Useful international communication involves curiosity without intrusive questions, clarity without unnecessary bluntness and respect without avoiding important facts. A brief written recap can prevent several days of avoidable confusion. Cultural sensitivity is not about memorising national stereotypes; it is about noticing ambiguity and creating shared understanding.''',
'''Partner A | We could perhaps consider Friday for the webinar.
Partner B | Great, I\'ll send out invitations for Friday.
Officer | Before we do that, could I clarify whether Friday is proposed or confirmed?
Partner A | It is only proposed. Our technical team hasn\'t confirmed availability.
Partner B | Thank you for clarifying. I misunderstood the suggestion as a decision.
Officer | No problem. Let\'s mark it as provisional until both teams confirm.
Partner A | That works for us. Could we receive a short recap?
Officer | Certainly. I\'ll email the proposed date and the outstanding confirmations.''',
('Degrees of certainty','Степени уверенности','Could, may and perhaps express possibility. Is confirmed or have agreed indicates a decision; do not treat polite suggestions as commitments.','We could consider Friday.;The date may change.;The meeting is confirmed for Friday.','Avoid interpreting “perhaps” as final agreement.',Q('Which expression signals only a possibility?','We could perhaps consider Friday.','Friday is confirmed for everyone.','We have formally agreed on Friday.','Perhaps and could do not mean confirmed.')),
[Q('What caused the problem?','A proposal was mistaken for a confirmed date.','The meeting software failed.','A partner refused to work with the other.','The problem was ambiguous commitment language.'),Q('What is the recommended cross-cultural strategy?','Ask, listen and confirm rather than rely on stereotypes.','Assume national cultures always behave identically.','Never clarify because it seems impolite.','Individual context matters more than simplistic labels.')],
[Q('Why is Friday not confirmed?','Technical team availability is still unknown.','The date is a public holiday everywhere.','The invitation list is already final.','The partner explicitly states that availability is pending.'),Q('What will the officer send?','A written recap of the proposal and pending checks.','A signed final approval document.','A cancellation of all webinars.','A recap creates shared understanding.')],
'Clarify a misunderstanding caused by indirect language and write a factual follow-up identifying what is proposed versus agreed.',
'A partner politely suggests a date. A colleague thinks it is final. Intervene tactfully and check expectations.',
'Thank you both. Just to make sure we are aligned, is Friday a confirmed date or an option we are still considering? If technical availability is not yet confirmed, I suggest we describe it as provisional in our follow-up email.',
'Write a short summary email that prevents another misunderstanding about a provisional webinar date.',
'Dear Colleagues, Thank you for discussing the joint webinar today. Friday is currently a proposed option, not a confirmed date. The speaker and technical teams still need to check their availability. Once we receive confirmation from both sides, we can finalise the invitation. Please let me know if this summary does not reflect your understanding. Kind regards, Alex',
('We perhaps can to choose Friday.','We could perhaps choose Friday.','After modal could, use the base verb without to.'),
Q('A colleague misreads a tentative suggestion as a firm commitment. What should you do?','Clarify the commitment level without blaming either person.','Accuse one nationality of being unclear.','Let incorrect invitations be sent.','Neutral clarification protects collaboration.')))
