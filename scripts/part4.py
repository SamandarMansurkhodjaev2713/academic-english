from authoring import make,Q
LESSONS=[]
LESSONS.append(make(
23,'Explaining Complex Procedures','Объяснение сложных процедур','explaining multistep academic processes',
'''step-by-step | пошаговый | Explained in a clear sequence of stages. | Please follow the step-by-step instructions.
prerequisite | предварительное условие | Something that must happen before the next step. | Identity verification is a prerequisite for access.
exceptional case | исключительный случай | A situation outside normal procedures. | Exceptional cases are referred for review.
verify | проверять | To check facts against an approved source. | We verify the registration details first.
submit evidence | предоставить подтверждения | To provide supporting documents or information. | Applicants submit evidence through the official channel.
conditional | условный | Depending on a requirement being met. | Approval may be conditional on complete records.
relevant office | профильный отдел | The department responsible for the issue. | Contact the relevant office for academic approval.
processing stage | этап обработки | The current part of an administrative workflow. | Your application is at the verification stage.
break down | разбить на части | To explain something complex in simpler components. | Break down the procedure into three actions.
final approval | окончательное утверждение | The last authorised decision in a process. | Final approval belongs to the academic committee.''',
'''I\'ll break the process into three steps. | Я разобью процесс на три шага.
Before you begin, please check… | Перед началом проверьте…
Once that is complete, you can… | Когда это будет завершено, вы сможете…
The next stage depends on… | Следующий этап зависит от…
In exceptional cases, please contact… | В исключительных случаях обратитесь к…
Does that sequence make sense? | Понятна ли такая последовательность?''',
'Turning a complicated procedure into clear guidance',
'''A visiting academic adviser asks the support office how a student can request recognition of prior study. The complete official policy is long and includes several decision points. Reading the policy aloud would be unlikely to help. The Academic Support officer first identifies the information the visitor actually needs: where the student starts, which evidence is required and who can decide the outcome.
The officer explains the process in three stages. First, the student reviews the current eligibility guidance and checks whether the relevant study falls within the published scope. Second, they submit the required academic records and module information through the approved channel. Third, the authorised academic team evaluates equivalence and communicates a decision. In some cases, additional information may be requested. The officer makes clear that submitting documents is not the same as receiving approval.
After the explanation, the visitor asks what happens when the module information is incomplete. The officer describes the likely next step carefully: the team may request more evidence, but local policy determines what is acceptable. The officer offers to share the official written procedure and summarises the three stages again. Clear procedure explanations combine sequencing, plain language and honest limits. They give people a mental map of the process without pretending every exception can be decided immediately.''',
'''Adviser | Could you explain the recognition-of-prior-study procedure in simple terms?
Officer | Certainly. There are three stages: check eligibility, submit evidence and wait for academic review.
Adviser | What sort of evidence is typically required?
Officer | The published guidance lists academic records and module information. Requirements may vary by case.
Adviser | Does completing the form mean the request is approved?
Officer | No. Approval follows a separate academic review.
Adviser | What if the module information is incomplete?
Officer | The team may request more evidence. I\'ll share the official guidance and the right contact details.''',
('Sequencing with once, before and after','Временные связки процедур','Use before, once, after and if to explain dependencies. Keep each sentence focused on one action.','Before submitting, check eligibility.;Once the file is complete, it can be reviewed.;If evidence is missing, the team may request it.','Do not use “once” to imply approval that has not happened.',Q('Which sentence shows the correct sequence?','Once the file is complete, the team can review it.','Once the file will complete, the team review it.','Once completing the file, approval is guaranteed.','Once introduces a completed prerequisite, not a promise.')),
[Q('What are the three main stages?','Eligibility, evidence and academic review.','Accommodation, sports and graduation.','Payment, transport and certification only.','The officer presents a three-stage process.'),Q('What could happen if information is incomplete?','The authorised team may request more evidence.','The application is automatically approved.','The support officer changes the academic rule.','The text describes possible additional verification.')],
[Q('Does submission mean approval?','No, a separate academic review is needed.','Yes, automatically.','Only if the student calls first.','The officer explicitly distinguishes submission from decision.'),Q('What does the officer offer after explaining?','Official guidance and contact details.','An unofficial guarantee.','A replacement degree.','Written guidance complements verbal explanation.')],
'Explain a complex academic procedure in three numbered stages, with a condition and an authorised decision point.',
'A partner asks how recognition of prior study works. Give a clear explanation without legalistic jargon.',
'First, the student checks the eligibility guidance. Next, they submit the required academic evidence through the approved route. Once the file is complete, the authorised team reviews it. If additional information is needed, the team may contact the student. Academic Support can explain the steps, but it cannot guarantee approval.',
'Draft a plain-English instruction message for a three-stage recognition request with a warning about final approval.',
'Dear Student, To request recognition of prior study, please first review the eligibility requirements in the current academic guidance. Next, submit the requested records and module details using the approved request form. The academic team will review complete applications and may ask for additional information. Submitting the form does not guarantee approval. Please contact Academic Support if you need help finding the instructions. Kind regards, Academic Support',
('Once you will submit the documents, we can review.','Once you submit the documents, we can review.','After once in a future-time clause, use Present Simple.'),
Q('Someone asks you to simplify a long official policy. What should you do?','Explain the main stages, dependencies and authorised decision point.','Read every clause aloud without pause.','Promise every outcome.','Plain-language sequencing supports understanding.')))
LESSONS.append(make(
24,'Giving Updates & Reporting Progress','Отчёты о ходе работы','status updates and action tracking',
'''completed | завершённый | Finished successfully. | The registration checks are completed.
in progress | в процессе | Currently being worked on. | The timetable revision is in progress.
pending | ожидающий | Waiting for further action or a decision. | The room allocation is pending approval.
blocker | препятствие | Something preventing a task from continuing. | Missing data is the main blocker.
owner | ответственный | The person or team assigned to an action. | The records team is the owner of this task.
milestone | контрольная точка | A meaningful stage in a project or process. | Confirming the list is our next milestone.
expected date | предполагаемая дата | A date that is anticipated but not necessarily confirmed. | We have an expected date, not a guarantee.
escalation | эскалация | Passing an issue to a higher authority when needed. | An escalation may be necessary if the deadline is at risk.
status report | отчёт о статусе | A concise summary of current work. | The weekly status report lists completed and pending tasks.
next action | следующее действие | The specific step someone should take next. | Each item in the report needs a next action.''',
'''The first stage has been completed. | Первый этап завершён.
The remaining items are still in progress. | Остальные пункты ещё в работе.
We are waiting for confirmation from… | Мы ожидаем подтверждения от…
The main blocker is… | Основное препятствие —…
The next action is assigned to… | Следующее действие закреплено за…
I\'ll provide another update on… | Я предоставлю следующее обновление…''',
'An honest update for a programme coordinator',
'''An academic programme coordinator asks for an update on preparations for an international staff workshop. The Academic Support officer has several pieces of information but no single summary. The invitation has been sent, the speaker list has been checked, the room booking is still awaiting approval and the final timetable has not been distributed. Without a structured update, the coordinator may incorrectly assume that every task is complete.
The officer prepares four brief sections: completed, in progress, blockers and next actions. Confirmed work is described in the past or present perfect, while pending tasks are clearly labelled. The room booking is a blocker because it prevents the team from finalising the invitation details. The officer identifies the scheduling team as the responsible owner and asks for a realistic update date. They avoid treating a suggested date as a guarantee.
During the meeting, the coordinator wants to know whether the workshop is at risk. The officer explains that the event can continue to be prepared, but the room decision needs follow-up. This gives the coordinator an accurate basis for choosing an action. Good reporting is not a list of everything staff have done. It highlights what changed, what is still unknown, who owns the next step and when another update should be expected. This is especially valuable in international work across teams and time zones.''',
'''Coordinator | Can you give me the status of our workshop preparation?
Officer | Certainly. Invitations have been sent and the speaker list is confirmed.
Coordinator | What is still in progress?
Officer | The final timetable is being updated, and room approval is still pending.
Coordinator | Is anything blocking the next step?
Officer | Yes, we need room confirmation before the revised invitation can be finalised.
Coordinator | Who is following up, and when will we hear more?
Officer | The scheduling team owns the approval. I\'ll request an update and report back on Thursday.''',
('Present Perfect for completed work','Present Perfect в отчётах','Use Present Perfect to report completed work with current relevance. Use Present Continuous for ongoing actions and simple forms for status labels.','We have sent the invitations.;The timetable is being updated.;Room approval is still pending.','Avoid saying “has been completed” for work that is still in progress.',Q('Which sentence accurately reports a finished action?','We have sent the invitations.','We sending invitations already.','We have send the invitations.','Present Perfect is have + past participle.')),
[Q('What is the main blocker?','Room booking approval.','The speaker list.','A missing student essay.','The room decision prevents final invitation details.'),Q('What is the best structure for a status report?','Completed, in progress, blockers and next actions.','Only completed tasks.','A long unstructured story.','The chosen categories distinguish facts and next steps.')],
[Q('What has been confirmed?','The speaker list.','The room approval.','The final timetable.','The officer states the speaker list is confirmed.'),Q('Who owns the room-approval follow-up?','The scheduling team.','The visiting speaker.','Any student.','The owner is explicitly named.')],
'Give a 60-second workshop status update with completed tasks, an in-progress item, one blocker and an owner.',
'Your manager asks for progress. Speak using four short status categories and make uncertainty visible.',
'Invitations have been sent and the speaker list is confirmed. The final timetable is still being updated. Room approval remains a blocker, and the scheduling team owns the next step. I will request an update and report back on Thursday.',
'Write a concise progress report to an academic manager distinguishing completed, pending and next actions.',
'Subject: Workshop preparation — status update\nDear Coordinator, The invitations have been sent and the speaker list is confirmed. The final timetable is in progress. Room allocation remains pending with the scheduling team and currently prevents us from finalising the revised invitation. I have requested an update and will share the next confirmed information on Thursday. Kind regards, Alex',
('We have send the invitations.','We have sent the invitations.','Present Perfect requires a past participle: sent.'),
Q('A coordinator assumes a pending task is completed. What should you say?','Correct the status clearly and identify the owner and next step.','Agree to avoid an awkward conversation.','Leave the status ambiguous.','Accurate reporting is more important than apparent certainty.')))
LESSONS.append(make(
25,'Handling Complaints Professionally','Профессиональная работа с жалобами','complaint handling and accountability',
'''complaint | жалоба | A formal or informal statement that something is wrong. | The student filed a complaint about the process.
acknowledgment | подтверждение получения | A message recognising that a report has been received. | We sent an acknowledgment of the complaint.
investigate | расследовать; изучить | To examine facts to understand a situation. | The responsible team will investigate the issue.
resolution | решение проблемы | An outcome intended to address a problem. | We cannot promise a resolution before review.
escalation route | путь эскалации | The approved way to send a serious issue for higher review. | The handbook explains the escalation route.
impartial | беспристрастный | Fair and not taking sides without evidence. | The review should be impartial.
record of contact | запись об обращении | A factual note of a communication. | Keep a professional record of contact.
response timeframe | срок ответа | The expected interval for a reply. | Check the published response timeframe.
respectful tone | уважительный тон | Language that treats the other person with dignity. | A respectful tone matters during complaints.
prevent recurrence | предотвратить повторение | To reduce the chance that a problem happens again. | We reviewed the process to prevent recurrence.''',
'''Thank you for raising this concern. | Спасибо, что сообщили об этой проблеме.
I understand this has caused inconvenience. | Я понимаю, что это вызвало неудобства.
We will follow the published complaints procedure. | Мы будем следовать официальной процедуре рассмотрения жалоб.
I cannot comment on the outcome before review. | Я не могу комментировать результат до проверки.
You will receive an acknowledgment. | Вы получите подтверждение получения обращения.
Here is how to request a formal review. | Вот как запросить официальный пересмотр.''',
'A complaint that needs careful handling',
'''An international student submits a complaint alleging that an important academic request was handled unfairly. The Academic Support officer is the first person to receive the message. They should acknowledge receipt and explain the official complaints process, but they should not decide immediately whether the allegation is correct. Fairness requires an impartial review by the appropriate people.
The student\'s email includes personal details about another student. The officer avoids copying that information into a broad departmental thread and follows the institution\'s confidentiality rules. They explain how the student can provide relevant evidence through the approved channel. They also check the published response timeframe before giving a date. If the complaint involves a serious safety or welfare concern, the staff member should follow the institution\'s separate safeguarding or urgent escalation procedure.
The officer\'s reply is short and respectful. It confirms that the concern has been received, indicates the next step and identifies where the student can find the complaint policy. It does not include an apology that falsely admits facts not yet established, nor does it dismiss the student\'s experience. “Thank you for bringing this to our attention” recognises the concern without prejudging the outcome. A strong complaint response supports the person, protects the integrity of the process and makes the route to review clear.''',
'''Student | I want to make a complaint. I believe my request was handled unfairly.
Officer | Thank you for telling us. I understand this is an important concern.
Student | Can you tell me now who was responsible?
Officer | I cannot make that finding before an impartial review. I can explain the formal procedure.
Student | I\'ve included another student\'s private details in my message.
Officer | We\'ll handle the information according to the university\'s confidentiality rules and approved channels.
Student | When can I expect a response?
Officer | I\'ll check the published timeframe and confirm the next steps rather than give an unverified date.''',
('Neutral and factual language','Нейтральные формулировки','Use factual wording and distinguish an allegation from a confirmed finding. “You reported…” is safer than “It has been proved…” before review.','Thank you for raising the matter.;Your concern will be reviewed through the approved process.;I cannot confirm a finding at this stage.','Avoid prejudging a complaint or sharing private details beyond authorised recipients.',Q('Which sentence avoids prejudging an allegation?','Your concern will be reviewed under the published procedure.','We have proved you are right without checking.','Your complaint is false and will be ignored.','Neutral language preserves impartiality.')),
[Q('Why should the officer not decide whether the complaint is true immediately?','An impartial review by authorised people is needed.','Because complaints should never be reviewed.','Because the officer dislikes written messages.','Procedural fairness requires investigation.'),Q('How should another student’s private details be treated?','Confidentially under approved rules.','Forwarded to a public group.','Published as supporting evidence.','Personal information must be handled appropriately.')],
[Q('What does the officer promise about timing?','To check the published response timeframe.','A decision within one hour.','An automatic refund.','The officer avoids inventing a date.'),Q('Can the officer identify responsibility before review?','No, not reliably.','Yes, immediately.','Only by asking other students.','The officer states that findings need an impartial review.')],
'Acknowledge a serious complaint, outline the formal route and describe the next action without making findings.',
'A student says they were treated unfairly. Give an impartial, empathetic first response and protect confidentiality.',
'Thank you for raising this concern. I understand that the situation is important to you. I can explain the formal complaints procedure and show you how to submit evidence securely. An authorised team will review the matter; I cannot determine the outcome in advance.',
'Draft a first acknowledgment email for a complaint about a delayed academic request.',
'Dear Student, Thank you for contacting us regarding your academic request. We acknowledge receipt of your concern. The university\'s published complaints procedure explains the review process and how to provide supporting information through the appropriate channel. We will confirm the applicable response timeframe and next steps. Please avoid sharing other students’ private information in general correspondence. Kind regards, Academic Support',
('We will investigate on the complaint.','We will investigate the complaint.','Investigate takes a direct object without on.'),
Q('You receive a complaint naming another student. What should you prioritise?','Confidential handling and the impartial approved review route.','Publicly discuss both students.','Guarantee a finding before investigation.','Confidentiality and due process take priority.')))
LESSONS.append(make(
26,'Negotiating Practical Arrangements','Согласование рабочих условий','practical coordination and compromise',
'''propose | предлагать | To put forward an option for consideration. | I would like to propose an alternative time.
constraint | ограничение | A condition that limits available options. | Room capacity is our main constraint.
flexible | гибкий | Able to adjust plans to accommodate needs. | We can be flexible about the workshop start time.
compromise | компромисс | An arrangement where each side adjusts something. | The teams reached a compromise on the schedule.
availability window | доступный временной интервал | A period during which someone can participate. | Please share your availability window.
minimum requirement | минимальное требование | A condition that must be satisfied. | Accessibility is a minimum requirement for the room.
alternative arrangement | альтернативная организация | Another practical plan to reach the goal. | We may need an alternative arrangement.
confirm in writing | подтвердить письменно | To record an agreement in a message or document. | Please confirm the final time in writing.
trade-off | компромисс между факторами | A choice balancing competing advantages. | The earlier slot has a trade-off for remote colleagues.
mutually convenient | удобный для обеих сторон | Suitable for all people involved. | We hope to find a mutually convenient date.''',
'''Would an earlier time be possible? | Можно ли назначить время пораньше?
Our main constraint is room capacity. | Наше главное ограничение — вместимость аудитории.
Could we explore an alternative? | Можем ли рассмотреть альтернативу?
That could work if we confirm the equipment. | Это подойдёт, если мы подтвердим оборудование.
Let\'s find a mutually convenient option. | Давайте найдём удобный для всех вариант.
I\'ll confirm the final arrangement in writing. | Я письменно подтвержу итоговую договорённость.''',
'Finding a workable venue for a joint workshop',
'''Two universities are planning a professional development workshop for academic staff. The host institution has a suitable room on Wednesday, but the visiting team is only available on Thursday. The Thursday room is smaller and may not support the required video equipment. The Academic Support officer is asked to coordinate a practical solution, not negotiate a new institutional agreement.
The officer begins by listing the non-negotiable requirements: accessible seating for all participants, reliable video conferencing and sufficient time for discussion. Next, they identify flexible factors: the workshop could start earlier, or part of the programme could be moved online. They present the options neutrally and explain the trade-offs. An earlier start may accommodate the visitors, but the technical team still needs to confirm equipment availability.
Rather than asking either side to agree immediately, the officer requests the necessary checks. Once the technical and events teams confirm what is possible, the organisers can choose a mutually convenient arrangement. The officer then records the agreed date, time, room and equipment responsibilities in a written follow-up. Practical negotiation often means making constraints explicit, exploring alternatives and avoiding premature promises. The language of proposals is collaborative: “Could we consider…?”, “Would it be possible…?” and “This may work if…”. Such phrases are useful for coordinating academic events.''',
'''Visitor | Thursday is the only day our lecturers can attend.
Officer | Understood. Our Thursday room is smaller, so we need to check capacity and equipment.
Visitor | Could we start earlier to use the larger room?
Officer | That\'s one option. I can ask the events team about availability.
Visitor | We also need a reliable video connection for remote colleagues.
Officer | Absolutely. That is a minimum requirement, so I\'ll involve the technical team.
Visitor | When can we confirm the arrangement?
Officer | Once the checks are complete, the organisers can decide. I\'ll confirm the details in writing.''',
('Second conditional for alternatives','Гипотетические варианты','Use the second conditional for hypothetical options: if + Past Simple, would + base verb. Use real-condition language for steps that are likely to happen.','If we started earlier, we would have more time.;If the room is available, we can confirm it.;We could use a hybrid format.','Do not confuse an imagined option with an already agreed arrangement.',Q('Which sentence correctly presents a hypothetical option?','If we started earlier, we would have more time.','If we start earlier, we would had more time.','If we starting earlier, we more time.','Second conditional uses if + Past Simple and would + base verb.')),
[Q('Which factor is non-negotiable?','Accessible space and functioning video support.','The officer’s preferred lunch break.','The exact colour of the chairs.','The essential requirements enable participation.'),Q('What happens after the teams verify options?','The organisers choose and confirm an arrangement.','The support officer signs a new agreement.','Everyone assumes Thursday is approved.','Verification precedes a final decision.')],
[Q('Why is the Thursday room difficult?','It is smaller and its equipment is unconfirmed.','It is already full of students.','It has no address.','The officer describes capacity and equipment limits.'),Q('Who will check the video equipment?','The technical team.','The student union only.','A visiting lecturer alone.','The technical team is named as responsible.')],
'Find an event arrangement that respects a fixed visitor date, accessibility and technical requirements.',
'Present two practical scheduling options and explain one condition that still needs to be checked.',
'Thursday works best for the visitors. One option is to use the smaller room if capacity and video equipment are confirmed. Another option is to start earlier in the larger room, if it is available. I will check the constraints with our events and technical teams before we confirm anything.',
'Write a partner email presenting two possible workshop arrangements and identifying pending checks.',
'Dear Colleagues, Thank you for sharing your availability. We are exploring two options for Thursday: an earlier session in the larger room or the originally proposed time in the smaller room. Both options depend on room capacity and video-equipment checks. We will confirm the final arrangement after the relevant teams have reviewed availability. Kind regards, Alex',
('If we would start earlier, we would finish sooner.','If we started earlier, we would finish sooner.','Do not normally use would in the if-clause of a second conditional.'),
Q('Two scheduling options are possible but unverified. How should you describe them?','As proposals subject to capacity and technical checks.','As guaranteed final arrangements.','As impossible without any enquiry.','Negotiation is transparent about constraints.')))
LESSONS.append(make(
27,'Academic Meetings & Decision Making','Совещания и принятие решений','agendas, minutes and action owners',
'''agenda item | пункт повестки | A specific topic for discussion at a meeting. | The first agenda item concerns orientation.
minutes | протокол встречи | A written summary of what was discussed and decided. | The minutes record the agreed actions.
action item | задача по итогам встречи | A specific task assigned after a discussion. | Each action item needs an owner and deadline.
chairperson | председательствующий | The person who leads a meeting. | The chairperson moved the discussion to the next item.
decision | решение | A choice that has been agreed or formally made. | The decision was recorded in the minutes.
proposal | предложение | An idea put forward but not necessarily accepted. | The proposal will be reviewed next week.
assigned owner | назначенный ответственный | The person accountable for completing a task. | The assigned owner will update the timetable.
due date | срок выполнения | The expected date for completing an action. | The action item has a due date of Friday.
approval | утверждение | Formal permission from an authorised person or group. | The proposal still needs departmental approval.
follow-up meeting | последующая встреча | A later session to review progress. | We scheduled a follow-up meeting for next month.''',
'''Let\'s move to the next agenda item. | Перейдём к следующему пункту повестки.
Can we confirm what has been decided? | Можем уточнить, какое решение принято?
Who will take ownership of this action? | Кто возьмёт ответственность за эту задачу?
What is the agreed due date? | Какой согласованный срок?
I will record that in the minutes. | Я внесу это в протокол.
That remains a proposal rather than a decision. | Это пока предложение, а не решение.''',
'An action item without an owner',
'''At a cross-departmental meeting, staff discuss ways to improve orientation for new international students. One participant suggests adding an online information page. Several people say that the idea sounds useful, but nobody agrees who will prepare the content. The Academic Support officer is responsible for writing the meeting minutes and notices the missing action owner.
Before the meeting ends, the officer asks the chair to confirm whether the page has actually been approved or only proposed. The group agrees to develop a draft for review, but final publication still requires the normal approval process. A colleague from student services accepts responsibility for the draft and agrees on a due date. Another colleague will review accessibility and language clarity.
The officer\'s minutes distinguish three categories: decisions made, proposals to be reviewed and actions assigned. Each action includes a task, an owner and a due date. This structure is more useful than a paragraph saying, “The team discussed orientation improvements.” The officer shares the draft minutes with the appropriate participants and invites factual corrections. If a decision was not made, the notes must not present it as confirmed. Clear meeting language helps prevent work from disappearing between departments. It also supports continuity when some colleagues join online or are unable to attend the full discussion.''',
'''Chair | We have discussed adding a new orientation information page.
Officer | Before I record the minutes, has publication been approved, or are we preparing a draft?
Chair | Only the draft has been agreed. Final publication still needs review.
Student Services | I can prepare the first draft by next Wednesday.
Officer | Thank you. Who will check accessibility and language clarity?
IT Colleague | I can review accessibility, and Alex can review the wording.
Officer | Great. I\'ll record the task, owners and due date separately from the publication decision.
Chair | Please circulate the draft minutes for confirmation.''',
('Reported speech in minutes','Косвенная речь в протоколах','Use neutral reported speech for meeting summaries: “The team agreed to…” or “It was proposed that…”. Do not attribute a final decision to an unapproved suggestion.','The team agreed to prepare a draft.;The chair confirmed that approval was pending.;It was proposed that a page be created.','Avoid writing “approved” when participants only discussed an idea.',Q('Which minute accurately reports a proposal?','The team agreed to prepare a draft for review.','The page was officially published during the meeting.','All proposed changes were automatically approved.','A draft agreement is not the same as final publication approval.')),
[Q('What was agreed during the meeting?','To prepare a draft page for review.','To publish immediately without approval.','To cancel international orientation.','The group approves a draft only.'),Q('What makes a useful action item?','A clear task, owner and due date.','A vague topic with no owner.','Only a participant name.','Action tracking requires the three elements.')],
[Q('Who prepares the first draft?','Student Services.','The visiting university.','The registrar by default.','A student services colleague volunteers.'),Q('Is publication already approved?','No; final publication requires review.','Yes, it was published in the call.','Yes, no further step is needed.','The chair explicitly distinguishes draft from publication.')],
'Write meeting notes that distinguish a decision from a proposal and include action owners and due dates.',
'You are taking minutes for a university meeting. Ask clarifying questions before recording a decision.',
'Could I confirm whether we have approved publication or only agreed to prepare a draft? Who will own the draft, and what is the due date? I will record the action separately from any approval still required and circulate the minutes for factual confirmation.',
'Draft a concise meeting-minutes section with a decision, two assigned actions, owners and dates.',
'Meeting note — Orientation information page. Decision: prepare a draft for review; publication not yet approved. Action 1: Student Services will prepare the first draft by Wednesday. Action 2: IT will review accessibility, and Academic Support will review language clarity by Friday. Final publication remains subject to the normal approval process.',
('The team agreed prepare a draft.','The team agreed to prepare a draft.','Agree is followed by to + infinitive when stating an action.'),
Q('The group discusses a suggestion but does not vote or approve it. How should minutes describe it?','As a proposal, with any agreed next-step tasks.','As a binding final decision.','As completed work.','Accurate minutes distinguish proposal from approval.')))
LESSONS.append(make(
28,'Unexpected Workplace Situations','Неожиданные рабочие ситуации','responding to uncertainty under pressure',
'''unexpected | непредвиденный | Not planned or anticipated. | We received an unexpected request before the meeting.
urgent enquiry | срочный запрос | A question that needs quick attention. | The urgent enquiry concerns a missing registration.
incomplete information | неполная информация | Facts that are not sufficient for a reliable answer. | We cannot confirm the situation with incomplete information.
contingency | резервный вариант | An alternative plan for a problem. | We need a contingency for the cancelled room.
escalate appropriately | корректно эскалировать | To pass an issue to the right authority. | We escalate appropriately when safety is involved.
prioritise | определять приоритет | To choose which tasks must be addressed first. | We prioritise requests based on urgency and impact.
verify first | сначала проверить | To confirm details before acting. | Verify first when a colleague asks for a record change.
reassure | успокоить; заверить в поддержке | To give truthful confidence or support. | Reassure the student without promising a result.
redirect | перенаправить | To move a request to a different process or person. | Redirect the request to the duty officer.
remain professional | сохранять профессионализм | To communicate appropriately under stress. | Try to remain professional during urgent calls.''',
'''Let me verify that before I respond. | Позвольте проверить это перед ответом.
I don\'t want to give you incorrect information. | Не хочу сообщить неверные сведения.
Here is what we know at the moment. | Вот что нам сейчас известно.
The next priority is… | Следующий приоритет —…
I will contact the responsible colleague. | Я свяжусь с ответственным сотрудником.
Thank you for your patience while we check. | Спасибо за терпение, пока мы уточняем.''',
'Three urgent requests before a visiting delegation',
'''Twenty minutes before an international delegation arrives, the Academic Support officer receives three messages. A classroom has become unavailable, a visiting lecturer cannot find the meeting link, and a student reports that a confidential document was sent to the wrong email address. All three problems need attention, but they are not equally serious or assigned to the same teams.
The officer first follows the institution\'s urgent privacy or incident-reporting procedure for the misdirected document, rather than trying to hide the problem or discussing it in a public chat. Next, they contact the event organiser and facilities team about a safe alternative room. Meanwhile, they resend the verified meeting link to the lecturer through the approved contact channel. The officer communicates what is confirmed, which actions are underway and which decisions require authorisation.
When the delegation arrives, the officer does not provide a dramatic account of the morning. They welcome the visitors, explain any practical change that affects them and direct them to the correct place. Later, they ensure that each issue has a documented owner and follow-up. Working under pressure does not mean answering immediately without checking. It means recognising risk, prioritising correctly and keeping language calm and accurate. Useful phrases include “Here is what we know so far” and “I will confirm that before giving you an answer.”''',
'''Colleague | The workshop room is suddenly unavailable, and the delegation arrives in twenty minutes.
Officer | I\'ll contact the event organiser and facilities team about an approved alternative.
Colleague | A lecturer also says the meeting link doesn\'t work.
Officer | I\'ll verify the current link and resend it through the established contact channel.
Colleague | We have another issue: a student record may have gone to the wrong address.
Officer | That needs immediate handling through our confidential incident-reporting procedure.
Colleague | What should we tell the visitors?
Officer | Only confirmed practical details. I\'ll update them when we have an approved room.''',
('Prioritising with clear sequencing','Приоритеты и факты','Use first, meanwhile, once confirmed and at the moment to separate immediate action from information still being checked. Avoid reporting guesses as established facts.','First, follow the incident procedure.;Meanwhile, I will verify the meeting link.;The new room is not confirmed yet.','Do not promise an alternative venue or a privacy outcome before verification.',Q('Which sentence accurately marks uncertainty?','The new room is not confirmed yet.','The new room is definitely ready without any checks.','Maybe guaranteed room is.','“Not confirmed yet” communicates the actual status.')),
[Q('Which problem requires the most sensitive handling?','A possibly misdirected confidential record.','The meeting link alone.','The missing name tags.','A potential privacy incident requires approved urgent procedures.'),Q('What is effective under pressure?','Verify, prioritise and communicate confirmed information.','Answer all questions by guessing.','Hide problems from responsible teams.','The reading emphasises controlled, accurate action.')],
[Q('Who should be contacted about the unavailable room?','The organiser and facilities team.','An admissions applicant.','A random lecturer overseas.','The officer names the operational owners.'),Q('What should the visitors hear?','Confirmed practical details.','Unverified rumours about the incident.','A promise that every problem is solved.','The officer limits communications to relevant confirmed facts.')],
'Triage three competing requests and give a calm update without exposing confidential information.',
'An important visitor is arriving while several tasks are failing. Describe your first actions and clearly separate fact from uncertainty.',
'First, I would follow the approved procedure for the confidential record issue. At the same time, I would ask the organiser and facilities team about an alternative room and verify the meeting link. I would tell the visitors only what is confirmed and provide a practical update when ready.',
'Write a brief internal status message with three priorities, responsible teams and one unresolved issue.',
'Internal update: A possible confidential-record incident has been referred through the approved urgent reporting route. Facilities and the event organiser are checking an alternative workshop room; this is not yet confirmed. The current online meeting link has been checked and resent to the lecturer. We will circulate only verified room details when available.',
('I will verify before I will answer.','I will verify before I answer.','In future-time clauses with before, use Present Simple.'),
Q('You cannot confirm a new room while visitors are arriving. What is best?','Explain that you are checking and give only confirmed directions.','Invent a room number to appear decisive.','Share private incident information with visitors.','Clarity about uncertainty prevents bigger problems.')))
LESSONS.append(make(
29,'Integrated Academic Support Simulation','Комплексная симуляция рабочего дня','integrated service day and communication decisions',
'''triage | сортировать по приоритету | To classify incoming requests by urgency and risk. | We triage the enquiries at the start of the day.
case reference | номер обращения | A unique identifier used to track a case. | Include the case reference in the follow-up.
handover | передача задачи | Giving responsibility and context to another colleague. | A clear handover prevents missed information.
coordinate across teams | координировать между отделами | To organise tasks involving several departments. | We coordinate across teams when requests overlap.
confirm scope | подтвердить полномочия | To clarify what work a team is responsible for. | Confirm scope before accepting an unusual request.
follow-through | доведение до результата | Continuing actions until an agreed next step is complete. | Good follow-through includes a final update.
action tracker | журнал задач | A record of assigned activities and status. | The action tracker shows who owns each case.
reconcile information | сопоставить сведения | To compare information and resolve differences. | We must reconcile information from two systems.
professional judgement | профессиональное суждение | Reasoned choices within an authorised role. | Professional judgement helps staff recognise escalation needs.
service continuity | непрерывность поддержки | Ensuring support continues even during changes. | The handover protects service continuity.''',
'''Let\'s prioritise the incoming requests. | Давайте расставим приоритеты для поступивших запросов.
I\'ll check which team owns the decision. | Я уточню, какой отдел отвечает за решение.
We have two sources that don\'t match. | У нас не совпадают данные из двух источников.
Could you confirm the case reference? | Не могли бы вы подтвердить номер обращения?
I\'ll document the agreed action points. | Я зафиксирую согласованные действия.
I\'ll close the loop with everyone concerned. | Я сообщу итог всем заинтересованным сторонам.''',
'A busy day across three universities',
'''The Academic Support officer starts the morning with five incoming matters. A visiting professor asks for an updated teaching timetable. An international student cannot see a registered module online. A partner university requests a student\'s official transcript. A coordinator wants to move an afternoon meeting, and the programme team asks for a short progress summary. These requests test different communication skills and involve different decision makers.
The officer begins by checking urgency, confidentiality and authority. The transcript cannot be sent to an unverified recipient, so the partner receives instructions for the official request channel. The student\'s online access problem is clarified by checking the registration record and directing the case to the learning-platform team if necessary. The timetable is checked against the latest approved version before it is shared with the professor. The meeting can be rescheduled only after the participants confirm availability.
At midday, the officer sends a status summary identifying completed actions, pending checks and task owners. One issue remains unresolved: the module appears in the official system but is missing online. The officer does not close that case until the responsible team confirms a fix and the student can access the materials. The day illustrates a central principle of Academic Support communication: being helpful does not mean independently approving everything. It means directing accurate information, protecting privacy, coordinating the right colleagues and ensuring people understand the next step.''',
'''Professor | Could you send me the latest timetable before my afternoon seminar?
Officer | Yes. I\'ll verify the approved version and send the current file.
Student | My module is registered, but I can\'t access it online.
Officer | Let\'s confirm the module code and log the access issue through the proper support channel.
Partner | Can you email a student\'s official transcript directly to me?
Officer | Official records require an authorised request. I\'ll explain the secure procedure.
Coordinator | Could we move today\'s meeting to 16:00?
Officer | I\'ll check everyone\'s availability before confirming the change.
Manager | Please give me a brief status report at midday.
Officer | Certainly. I\'ll separate completed items, pending checks and assigned next actions.''',
('Mixed tenses for workplace reporting','Смешанные времена в рабочих ситуациях','Choose tense by meaning: Present Simple for responsibilities, Present Perfect for completed actions, Present Continuous for ongoing tasks, and will for immediate commitments.','We handle academic enquiries.;I have sent the timetable.;The team is checking access.;I will email the update.','Avoid using one tense for every status regardless of meaning.',Q('Which report sentence correctly describes a completed action?','I have sent the verified timetable.','I sending the verified timetable yesterday now.','I have send the timetable.','Present Perfect reports a completed action relevant to the present.')),
[Q('Which request needs secure handling?','A partner’s request for a student\'s official transcript.','The professor’s public timetable.','A meeting time proposal.','Academic records are confidential.'),Q('When can the module access case be closed?','After the team confirms a fix and the student can access materials.','When the request is forwarded, regardless of outcome.','Before checking registration.','Closing the loop requires outcome verification.')],
[Q('What does the coordinator want to change?','An afternoon meeting time to 16:00.','The academic grading scale.','The transcript request policy.','The coordinator asks about moving the meeting.'),Q('What must be checked before confirming?','Everyone’s availability.','Only the officer’s personal preference.','The workshop food order.','Availability determines whether the new time is feasible.')],
'Complete a simulated service day: prioritise five requests, reply to different stakeholders and document follow-up.',
'Give a 90-second briefing to your manager explaining how you handled an official transcript request, an access issue and a timetable request.',
'Today I prioritised requests based on urgency and confidentiality. I directed the transcript enquiry to the official records process and verified the timetable before sending it. The student\'s online module issue is still being investigated by the relevant team. I will follow up after confirmation and keep the student updated.',
'Write a 120-word end-of-day update with three completed actions, one pending issue and an owner.',
'Subject: Academic Support — daily status\nDear Manager, Today we verified and shared the current teaching timetable, provided the official transcript-request procedure to our partner, and checked availability for the proposed meeting change. The module-access issue remains open: the student is registered, but the module is not yet visible online. The learning-platform team owns the technical investigation, and Academic Support will follow up with the student once a verified update is available. No confidential academic record was released outside the approved process. Kind regards, Alex',
('The team have sent the report and is checking now.','The team has sent the report and is checking now.','In this International English course, treat a team as singular for this construction to keep agreement consistent.'),
Q('Which decision best represents good Academic Support practice?','Coordinate the right teams and verify outcomes before closing cases.','Approve confidential releases without authorisation.','Close every case when an email is sent.','Accuracy, confidentiality and follow-through are essential.')))
LESSONS.append(make(
30,'Final Assessment & Development Plan','Итоговая проверка и дальнейший план','integrated communication assessment and reflection',
'''learning outcome | учебный результат | A skill or ability a learner is expected to demonstrate. | The learning outcomes focus on practical communication.
baseline | исходный уровень | A starting measurement used for comparison. | Compare the final check with the baseline assessment.
evidence of progress | подтверждение прогресса | Actual work or results showing improvement. | Your recorded responses provide evidence of progress.
self-assessment | самооценка | Reflecting on your own work using explicit criteria. | Use self-assessment to review the role-play.
fluency | беглость | The ability to communicate smoothly with manageable pauses. | Fluency improves with repeated real tasks.
accuracy | точность | Using language correctly and precisely. | Accuracy matters when explaining deadlines.
reflection | рефлексия | Thoughtful review of what you learned and need next. | Write a reflection after your final challenge.
action plan | план действий | Concrete steps for future improvement. | The action plan includes weekly speaking practice.
measurable goal | измеримая цель | A target that can be checked using evidence. | Writing two professional emails is a measurable goal.
continued practice | регулярная практика | Ongoing learning after a course. | Continued practice helps new language remain usable.''',
'''Let me reflect on what I can do now. | Давайте оценим, что я теперь умею.
I have become more confident with… | Я стал(а) увереннее в…
I still need to improve… | Мне ещё нужно улучшить…
My next measurable goal is… | Моя следующая измеримая цель —…
I will practise this skill twice a week. | Я буду тренировать этот навык дважды в неделю.
I can demonstrate this through… | Я могу показать это на примере…''',
'What counts as meaningful language progress?',
'''At the end of a thirty-day learning programme, a staff member wants to know whether their English has improved. A single percentage does not tell the whole story. They may now be faster at explaining registration steps, more comfortable asking clarifying questions or more careful about promises in professional email. These are valuable outcomes even if they are not equivalent to an officially certified CEFR level change.
The learner compares their initial and final responses to comparable workplace situations. They examine evidence: whether their message includes the right facts, how clearly they explain next steps, and whether they use appropriate professional tone. Automatically scored vocabulary and comprehension questions add another source of information, but speaking and writing need rubrics and thoughtful self-review unless an appropriately validated evaluator is available.
The learner notices one strength: they can now explain academic procedures in a clear sequence. Their next development target is responding fluently in unpredictable meetings. They create a concrete plan: practise two short role-plays each week, review words due in the spaced-repetition system, and write one professional follow-up email every Friday. After each task, they record one thing that went well and one thing to improve. Learning does not finish with Day 30. The course provides a foundation for continued, measurable professional communication development.''',
'''Mentor | How would you describe your progress after this programme?
Learner | I can explain student request procedures more clearly and write more useful follow-up emails.
Mentor | What evidence supports that impression?
Learner | I can compare my first and last role-plays and review the task rubrics.
Mentor | Does that mean you have an official B2 certificate?
Learner | No. This course measures practice outcomes, not an officially validated CEFR qualification.
Mentor | What will you work on next?
Learner | I\'ll practise spontaneous meeting responses twice a week and review my vocabulary regularly.''',
('Reflection and future commitments','Рефлексия и планы на будущее','Use Present Perfect for progress achieved, still need to for remaining gaps, and will or be going to for future practice plans.','I have improved my email structure.;I still need to practise quick responses.;I will complete two role-plays each week.','Avoid claiming a formal B2 qualification from an informal course score.',Q('Which sentence accurately reflects achieved progress?','I have become more confident in meetings.','I have became more confident.','I becoming more confident since last month.','Present Perfect uses have + past participle, “become”.')),
[Q('Why is one percentage insufficient for measuring progress?','Professional communication includes several different skills and kinds of evidence.','Percentages are never useful.','Only vocabulary matters.','Skills and self-review complement automatically scored tests.'),Q('What is the learner’s next focus?','Spontaneous meeting responses.','A new undergraduate application.','Only memorising grammar terms.','The learner identifies fluency in unpredictable meetings as a target.')],
[Q('Does the course issue an official B2 qualification?','No; the assessment is an internal learning tool.','Yes; the course automatically certifies B2.','Yes, after a single role-play.','The dialogue distinguishes an informal learning profile from certification.'),Q('How often will the learner practise spontaneous responses?','Twice a week.','Once a year.','Every hour.','The learner names a twice-weekly plan.')],
'Complete the final assessment, compare learning evidence and create three realistic next-month goals.',
'Explain what you can now do better, which skill remains difficult, and how you will practise it after this course.',
'I have improved my ability to explain academic procedures and write professional follow-ups. I still need to speak more smoothly in unexpected meetings. My plan is to practise two role-plays every week, review vocabulary on schedule, and write one realistic email each Friday.',
'Write a 120-word professional development plan for the next 30 days with at least three measurable actions.',
'My next 30-day goal is to communicate more fluently with international university partners. I will complete two role-play conversations each week, focusing on clarification and meeting participation. Every Friday, I will write a professional follow-up email and check it against a four-point rubric. I will review due vocabulary items on at least five days each week. At the end of the month, I will repeat a comparable workplace scenario and compare clarity, accuracy and confidence with my first attempt. I will record specific improvements and select the next skill to practise.',
('I have became better at explanations.','I have become better at explanations.','The past participle of become is become.'),
Q('Which development goal is genuinely measurable?','Complete two meeting role-plays each week and review responses.','Get perfect at English immediately.','Be fluent sometime.','A measurable goal specifies an observable task and frequency.')))
