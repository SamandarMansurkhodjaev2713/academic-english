from authoring import make,Q
LESSONS=[]
LESSONS.append(make(
9,'Academic Policies & Procedures','Академические правила и процедуры','policy explanations and academic integrity',
'''policy | правило; политика учреждения | An official principle that guides decisions. | The attendance policy is published in the handbook.
procedure | процедура | The practical steps used to apply a rule. | The procedure explains how to submit an appeal.
academic integrity | академическая честность | Acting honestly in academic work and assessment. | Academic integrity includes proper acknowledgement of sources.
attendance requirement | требование посещаемости | A rule about participation in scheduled activities. | The module has an attendance requirement.
exception | исключение | An authorised departure from a general rule. | Exceptions need the appropriate approval.
appeal | апелляция | A formal request to review a decision. | The student asked about the appeals process.
comply with | соблюдать | To act according to a rule or requirement. | Students must comply with published assessment rules.
discretion | право решать по усмотрению | Authority to choose within allowed limits. | The coordinator has discretion in specific cases.
refer to the handbook | обратиться к справочнику | To check an official source for information. | Please refer to the handbook for the full policy.
formal request | официальное обращение | A request submitted through an approved procedure. | An exception may require a formal request.''',
'''According to the published policy… | Согласно опубликованным правилам…
The procedure involves three steps. | Процедура включает три этапа.
An exception may require approval. | Исключение может требовать согласования.
Please refer to the current handbook. | Пожалуйста, обратитесь к актуальному справочнику.
I can explain the process, not decide the outcome. | Я могу объяснить процесс, но не принять решение.
Would you like me to show you where to find the guidance? | Хотите, я покажу, где найти инструкцию?''',
'Explaining an attendance rule without overpromising',
'''A student is worried after missing several classes due to an unexpected family situation. They ask whether the Academic Support officer can simply remove the absences from the university record. The officer wants to respond with empathy, but must also respect the institution\'s rules and the privacy of the student\'s circumstances. A supportive response begins by acknowledging the concern rather than making an immediate decision.
The officer checks the current academic handbook before explaining the published attendance rule. The handbook distinguishes the general requirement from any procedure for requesting an exception. In this university\'s fictional example, supporting information may be required, and an authorised academic colleague makes the decision. The officer can help the student understand how to make a formal request, but should not claim that approval is guaranteed.
It is useful to separate a policy from a procedure. A policy states the principle; a procedure describes the steps a person needs to follow. Academic integrity guidance is another example: the policy sets expectations for honest work, while procedures describe how a possible violation is reviewed. Staff should avoid improvising legalistic explanations or sharing private case details with other students. A clear, respectful explanation helps the student understand their options and what evidence or action is needed. Rules can be communicated accurately without sounding cold or dismissive.''',
'''Student | I missed several classes. Can you remove those absences from my record?
Officer | I\'m sorry this has been difficult. Let me explain the attendance procedure.
Student | Does the policy allow exceptions?
Officer | The handbook describes a formal request process. An authorised academic colleague reviews each case.
Student | So if I submit a request, it will definitely be approved?
Officer | I can\'t guarantee the outcome, but I can show you the requirements and where to submit it.
Student | Should I explain my personal situation to everyone teaching the module?
Officer | Please follow the confidential channel described in the official guidance.''',
('Modals for rules and possibility','Модальные глаголы в правилах','Use must for clear requirements, may for permission or possibility, and should for advice. Distinguish a rule from a suggestion.','Students must follow assessment rules.;An exception may be possible.;You should check the current handbook.','Avoid using “will definitely” when an authorised review is pending.',Q('Which sentence avoids guaranteeing an exception?','An exception may be possible after review.','An exception will definitely be granted.','Every attendance rule is optional.','May expresses possibility rather than certainty.')),
[Q('What is the difference between policy and procedure?','A policy states a rule; a procedure sets out steps.','They always mean the same thing.','A procedure only applies to teachers.','The reading explicitly separates principles from processes.'),Q('Who decides on a requested exception?','An authorised academic colleague.','The support officer automatically.','Other students in the class.','Decision authority must be respected.')],
[Q('Does submitting a request guarantee approval?','No, an authorised person must review it.','Yes, all requests must pass.','Only if an officer promises it verbally.','The officer refuses to guarantee an outcome.'),Q('How should sensitive information be submitted?','Through the confidential official channel.','In a public group chat.','To all classmates.','Confidentiality is part of the guidance.')],
'Explain a policy and the steps for requesting an exception without making the decision yourself.',
'A worried student asks whether a missed-class exception will definitely be approved. Show empathy and explain the process.',
'I understand that you are concerned. The handbook explains the attendance requirement and the process for requesting an exception. I can help you find the correct form, but the authorised academic team will review the evidence and make the decision.',
'Draft a clear and empathetic email directing a student to the published attendance appeal procedure.',
'Dear Student, Thank you for explaining your concern. The current student handbook sets out the attendance requirements and the procedure for requesting a review. You can find the relevant guidance in the Academic Policies section. Please submit any sensitive supporting information through the approved confidential channel. The authorised team will evaluate your request. Kind regards, Academic Support',
('An exception will certainly approved.','An exception may be approved.','Use a modal plus be + past participle to express a possible passive outcome.'),
Q('Someone asks you to change a recorded absence immediately. What is appropriate?','Explain the formal process and who makes the decision.','Alter the record without a review.','Share the student’s circumstances publicly.','Follow policy, decision boundaries and confidentiality.')))
LESSONS.append(make(
10,'Documents & Administrative Requests','Документы и административные запросы','official records and document handling',
'''transcript | академическая выписка | An official record of courses and results. | The student requested an official transcript.
certificate | сертификат; справка | A document confirming an achievement or status. | The student needs a certificate of enrollment.
academic record | академическая запись | A formal record of a student\'s academic history. | Access to an academic record is restricted.
authenticate | удостоверять подлинность | To confirm that a document or identity is genuine. | The office may need to authenticate the document.
certified copy | заверенная копия | A copy officially confirmed as matching the original. | The partner asked for a certified copy.
processing time | срок обработки | The period required to complete a request. | Processing time is listed in the service guide.
request form | форма заявления | A form used to ask officially for a service. | Complete the request form before submitting it.
authorised recipient | уполномоченный получатель | Someone permitted to receive confidential information. | Send the record only to an authorised recipient.
issue a document | выдать документ | To officially provide a document. | The records office can issue the certificate.
track a request | отслеживать запрос | To monitor progress from submission to completion. | You can track a request using its reference code.''',
'''Could you specify which document you need? | Не могли бы вы уточнить, какой документ нужен?
Please submit the form through the official portal. | Подайте форму через официальный портал.
The processing time may vary. | Срок обработки может различаться.
Only authorised staff can access these records. | Только уполномоченные сотрудники имеют доступ к этим записям.
I can check the status using your reference number. | Я могу проверить статус по регистрационному номеру.
The records office issues official transcripts. | Официальные выписки выдаёт отдел документации.''',
'A partner requests a student\'s transcript',
'''A partner university asks Academic Support to email a student\'s official transcript directly to a visiting lecturer. The request sounds routine, but a transcript contains personal academic information. The support officer should not assume that the person making the request has permission to receive it. The correct action is to check institutional data-protection rules and the approved verification process.
The officer asks the requester to specify the document type and provides guidance on the formal request channel. A transcript, a certificate of enrollment, and a degree certificate confirm different things. Using the right term matters because the wrong document may not meet the partner\'s purpose. The officer also explains that document processing times depend on the service and cannot be promised without checking the current guide.
In this fictional situation, the student must authorise release through the official system before the records office can issue a document to a verified recipient. Academic Support can describe the requirements and help track the request, but it does not bypass identity checks. After the request is submitted, the officer can refer to its tracking number when following up. A professional reply includes clear instructions, a link or location for the correct procedure, and realistic expectations. Speed is helpful, but accuracy and confidentiality are more important.''',
'''Partner | We need a transcript for one of your students. Can you email it to my colleague?
Officer | I can explain the process. First, could you confirm which official document is required?
Partner | An academic transcript with the student\'s completed modules and results.
Officer | Thank you. Records are released only through our approved verification procedure.
Partner | Can Academic Support issue it directly?
Officer | The records office issues official transcripts. We can guide the request and help track its status.
Partner | Is there a fixed processing time?
Officer | It depends on the service. I\'ll check the current guidance and send you the details.''',
('Passive voice for procedures','Страдательный залог в официальных процедурах','Use be + past participle when the process or document matters more than the person performing the action. Use active voice when naming the responsible team makes the message clearer.','Records are released after verification.;The certificate is issued by the records office.;We check the request before forwarding it.','Avoid hiding responsibility in passive voice when the reader needs to know whom to contact.',Q('Which passive sentence is correct?','The document is issued by the records office.','The document is issue by the records office.','The document issued by the records office is.','Passive: be + past participle.')),
[Q('Why can the transcript not simply be emailed to anyone who asks?','Academic records require verified authorised access.','Transcripts never exist as PDFs.','Only lecturers can use email.','Student privacy and authorisation matter.'),Q('How does a certificate of enrollment differ from a transcript?','It confirms student status rather than listing full course results.','It contains the same information in all cases.','It is always a final degree.','The documents serve different purposes.')],
[Q('Who issues official transcripts?','The records office.','The support officer independently.','The visiting lecturer.','The dialogue explicitly names the issuing office.'),Q('What determines processing time?','The specific service and current guidance.','Only the student\'s age.','The requester’s preferred date.','The officer cannot promise a universal turnaround.')],
'Explain a secure transcript request process to an international partner and distinguish three document types.',
'A partner asks you to send a student\'s academic record to an unverified address. Explain the approved process politely.',
'I can help you locate the transcript request procedure. Because an official transcript contains personal academic information, it must be released through the approved verification process. The records office issues the document, and I can help you track the request.',
'Write a clear email explaining how a student can request a certificate of enrollment.',
'Dear Student, Thank you for contacting Academic Support. To request a certificate of enrollment, please use the official document request form in the student portal. The records team will verify your details and process the request according to the published service timeframe. If you experience difficulties submitting the form, please let us know. Kind regards, Academic Support',
('The transcript is issue after verification.','The transcript is issued after verification.','Passive voice requires be plus the past participle issued.'),
Q('An unfamiliar contact asks for a student record. What should you do?','Explain and use the official authorisation process.','Send the record immediately to be helpful.','Ask the whole class to verify it.','Privacy safeguards come before convenience.')))
LESSONS.append(make(
11,'Student Questions & Requests','Запросы студентов','student enquiries and guidance',
'''enquiry desk | стойка консультаций | A service point where people ask questions. | The enquiry desk directs students to support services.
request clarification | запросить уточнение | To ask for additional information so a request is clear. | We need to request clarification about the course code.
guidance | консультация; инструкция | Information that helps someone decide what to do. | The portal provides guidance on registration.
relevant | относящийся к делу | Directly connected to the issue. | Please attach the relevant page of the form.
accessible | доступный | Easy to reach, use or understand. | Instructions should be accessible to international students.
resolve | решить | To find a satisfactory answer or outcome. | We resolved the login issue with the IT team.
refer onward | перенаправить дальше | To send a person to a more appropriate service. | We refer welfare concerns onward to specialist support.
follow-up message | последующее сообщение | A message sent after an earlier conversation. | Send a follow-up message confirming the link.
confidential | конфиденциальный | Intended to be shared only with authorised people. | The student\'s circumstances are confidential.
next step | следующий шаг | The action that should happen after the current stage. | Please explain the next step in simple terms.''',
'''How can I help you today? | Чем я могу вам помочь сегодня?
Could you give me a little more detail? | Не могли бы вы рассказать подробнее?
Let me make sure I understand your request. | Давайте уточним, правильно ли я понимаю ваш запрос.
Here is the guidance for the next step. | Вот инструкция для следующего шага.
I can direct you to the right team. | Я могу направить вас к нужной команде.
Please let me know if you need further assistance. | Сообщите, если понадобится дополнительная помощь.''',
'One student, two different questions',
'''A first-year international student visits the Academic Support desk with a confusing question: “My course is not working.” That sentence does not reveal whether the problem is technical, academic or administrative. The officer welcomes the student and asks for a little more information. The student explains that a module is missing from the learning platform and they cannot access an assignment. Two separate issues may be involved.
The officer first asks whether the module appears in the student\'s official registration record. If it is missing there, the programme administration team may need to check the registration. If the module is registered correctly but inaccessible online, the learning technology or IT team may be the right contact. The officer should not request the student\'s password or ask them to disclose private account information at the desk.
To avoid confusion, the officer gives the student a short summary: check the official registration status, report any platform error through the approved service channel, and include the module code and a screenshot if permitted. The officer follows up with a message containing the relevant links. The student now understands that one broad complaint may contain several specific tasks. Asking the right questions is a practical skill; a fast answer is not always a useful answer.''',
'''Student | Hi. My course isn\'t working and I don\'t know what to do.
Officer | I\'m sorry to hear that. Could you tell me what happens when you try to open it?
Student | The module doesn\'t appear on the learning platform.
Officer | Is it listed in your official registration record?
Student | Yes, I can see it there, but not online.
Officer | Thanks. That helps us identify the issue. It may need a learning-platform check.
Student | Should I give you my account password?
Officer | No, please keep your password private. I\'ll show you the approved support channel.''',
('Open and closed questions','Открытые и закрытые вопросы','Use open questions to explore a problem, then closed questions to confirm facts. Combine both before recommending action.','What happens when you open the course?;Is the module listed in your record?;Could you show me the error message?','Do not ask for passwords or confidential details when unnecessary.',Q('Which question invites a detailed explanation?','What happens when you open the module?','Is your module visible: yes or no?','Do you have a password?','What happens…? is an open question.')),
[Q('What information helps identify the likely problem?','The module is registered but missing online.','The student dislikes the campus café.','The student has no registered programme.','The two systems need different support pathways.'),Q('Why is the initial question difficult to answer?','It is too broad to identify the type of problem.','It contains advanced grammar.','It names every relevant system.','Clarifying the actual symptom comes first.')],
[Q('Should the student share their password?','No, they should keep it private.','Yes, at the public desk.','Only with another student.','The officer directs the student to an approved support channel.'),Q('What kind of issue is suspected?','A learning-platform access issue.','An admissions interview.','A tuition refund.','The registration is already visible in the official record.')],
'Clarify an unclear student enquiry, identify the appropriate team and give two precise next steps.',
'A new student says, “Nothing works on my course page.” Ask useful questions and provide safe guidance.',
'Could you describe what you see when you open the module? Is it listed in your official registration record? Thank you, that helps. Please do not share your password. We can direct your report to the appropriate learning-platform support team.',
'Write a concise follow-up with two actions after a student reports a missing online module.',
'Dear Student, Thank you for visiting Academic Support. As discussed, please first confirm that your module appears in the official registration record. If it does, report the access problem through the learning-platform help channel, including the module code and a description of the error. Please do not send your password. Kind regards, Academic Support',
('Could you explain me the problem?','Could you explain the problem to me?','Explain takes the object followed by to + person.'),
Q('A student gives a vague complaint. What is the best first move?','Ask open questions to identify the precise issue.','Guess which department caused it.','Request the student’s password.','Diagnose the task before choosing a solution.')))
LESSONS.append(make(
12,'Grades & Academic Performance','Оценки и успеваемость','assessment and academic progress',
'''assessment | оценивание | A method for measuring learning, such as a test or assignment. | The module includes two assessments.
coursework | текущие учебные задания | Work completed during a course and used in assessment. | Coursework contributes to the final result.
grade | оценка | A mark or category representing assessed performance. | The grade is visible in the student portal.
feedback | обратная связь | Comments explaining strengths and areas for improvement. | The lecturer provides feedback after marking.
academic progress | учебная успеваемость | A student\'s advancement through academic requirements. | Advisers monitor academic progress each semester.
reassessment | повторное оценивание | Another permitted opportunity to be assessed. | The rules specify when reassessment is available.
grade release | публикация оценок | The date when results become available. | Grade release is scheduled for next week.
marking | проверка и выставление баллов | The act of evaluating a student\'s work. | Marking must be completed before results are published.
academic standing | академический статус по успеваемости | A formal status based on academic performance. | Academic standing may affect progression.
result query | запрос по результату | A request for information about a published result. | A result query is handled through an approved process.''',
'''The result has not yet been released. | Результат ещё не опубликован.
The lecturer is responsible for academic marking. | Преподаватель отвечает за оценивание работы.
You can find feedback in the student portal. | Обратную связь можно найти в студенческом портале.
Please check the published reassessment policy. | Проверьте опубликованные правила пересдачи.
I can explain the review procedure. | Я могу объяснить процедуру пересмотра.
Grading scales may differ by institution. | Шкалы оценивания могут различаться между университетами.''',
'Understanding a result without changing it',
'''A student contacts Academic Support after seeing a mark lower than expected. They ask the officer to increase the grade because they worked very hard. The officer acknowledges the disappointment but makes no promise about the result. Academic staff who assess the work, and authorised review bodies, have responsibilities that differ from those of an administrative support team.
The officer first distinguishes a grade from feedback. A grade records the assessed outcome; feedback explains how the work met particular criteria. If the student wants to understand the mark, reading the feedback may be a useful first step. If they believe a procedural problem occurred, the university may have a specific enquiry or appeal process. The officer should refer to current published rules rather than inventing a universal right to reassessment or a guaranteed increase.
The student also asks whether their mark is a pass at a partner university. The officer explains that grading scales vary between institutions and that official equivalence decisions belong to authorised academic colleagues. Finally, the officer summarises the relevant options and directs the student to the proper guidance. A good support conversation is calm and factual. The student may remain disappointed, but they receive an accurate explanation of the process and whom to contact next.''',
'''Student | I\'m unhappy with my coursework grade. Can you raise it for me?
Officer | I understand this is disappointing. Academic Support cannot change assessed grades directly.
Student | Then who can explain why I received this result?
Officer | Your lecturer\'s feedback may explain the assessment criteria. I can also show you the formal query process.
Student | Does a grade of 60 mean the same thing at our partner university?
Officer | Not necessarily. Grading scales differ, and authorised staff must confirm any equivalence.
Student | Can I apply for reassessment automatically?
Officer | Please check the published rules; eligibility depends on the applicable assessment policy.''',
('Contrast and caution: however, may, depends on','Контраст и осторожные формулировки','Use however for contrast, may for possibility, and depends on when conditions vary. These forms prevent overstatements.','The student worked hard; however, the grade is unchanged.;Reassessment may be available.;Eligibility depends on the policy.','Do not equate two grading scales without confirmation.',Q('Which sentence is appropriately cautious?','Eligibility depends on the assessment policy.','Every result can always be changed.','All grading scales are identical.','Depends on avoids pretending an uncertain rule is universal.')),
[Q('Who can directly adjust grades according to the example?','Authorised academic decision makers, not Academic Support.','Any staff member at reception.','International visitors without review.','Roles and review authority are distinct.'),Q('What is the difference between a grade and feedback?','A grade states a result; feedback explains performance.','They are always identical documents.','Feedback is only used for enrollment.','Feedback provides explanation beyond the mark.')],
[Q('Can Academic Support raise a grade directly?','No.','Yes, immediately.','Only by sending an informal message.','The officer explicitly states the limit.'),Q('Are partner-university grading scales automatically equivalent?','No, equivalence requires appropriate confirmation.','Yes, a number always has the same meaning.','Only if the student says so.','The conversation notes institutional variation.')],
'Explain a disappointing result, direct a student to feedback and distinguish a result query from a promised grade change.',
'A disappointed student asks you to change a result. Respond professionally, showing empathy and explaining legitimate options.',
'I understand that the result is disappointing. Our team cannot change assessed marks, but I can explain where to find the feedback and how to submit a formal result query if the relevant conditions apply. The authorised academic team will consider any review.',
'Write a respectful message explaining how to find feedback and where to ask about a possible assessment review.',
'Dear Student, Thank you for contacting us about your result. You can find the lecturer’s feedback in the assessment section of the student portal. If you believe there was a procedural issue, please read the published result-query guidance and follow the relevant steps. Academic Support can explain the process but cannot amend marks directly. Kind regards, Academic Support',
('The assessment depend of the policy.','The assessment depends on the policy.','Use depends on, not depend of; singular subject takes -s.'),
Q('A student asks if you can guarantee a reassessment. How should you answer?','Eligibility depends on the published rules; I can show you the process.','Yes, everybody gets a new attempt.','Grades are never reviewed anywhere.','Explain conditions rather than inventing an outcome.')))
LESSONS.append(make(
13,'Deadlines, Extensions & Submissions','Сроки, продления и подача заданий','academic deadlines and extensions',
'''deadline | крайний срок | The last permitted time to submit something. | The assignment deadline is Friday at noon.
extension | продление срока | Additional permitted time to complete a task. | A student requested an extension for the report.
submission | подача работы | The act of handing in a document or assignment. | Online submission closes at the stated time.
late penalty | штраф за просрочку | A reduction applied when work is submitted late under a policy. | The handbook explains any late penalty.
supporting evidence | подтверждающие материалы | Documents that support a request or explanation. | The process may require supporting evidence.
request in advance | запросить заранее | To ask for permission before a deadline. | Please request an extension in advance if required.
mitigating circumstances | смягчающие обстоятельства | Situations that may affect performance and are considered under policy. | The university has a process for mitigating circumstances.
eligible | имеющий право | Meeting formal conditions for something. | Eligible students can use the published request route.
portal timestamp | отметка времени в портале | The time automatically recorded for an online submission. | The portal timestamp confirms when the file arrived.
submit on time | подать вовремя | To provide required work before the deadline. | Please submit on time whenever possible.''',
'''When is the submission deadline? | Когда крайний срок подачи?
Could you explain the extension procedure? | Не могли бы вы объяснить процедуру продления?
Please submit your request before the stated date. | Пожалуйста, подайте запрос до указанной даты.
An extension is not automatically granted. | Продление не предоставляется автоматически.
The decision depends on the published policy. | Решение зависит от опубликованных правил.
Keep a record of your submission. | Сохраните подтверждение подачи.''',
'The deadline is approaching',
'''A student is preparing a major assignment but suddenly cannot finish it by the published deadline. They contact Academic Support the day before submission and ask for an automatic extension. The officer listens and explains that extensions are governed by an approved process. Some universities distinguish ordinary extensions from applications based on mitigating circumstances; the precise rules, evidence and decision makers vary.
The officer asks the student to check the current deadline, including the exact time and time zone shown in the system. Submitting one minute late can matter if the rules use an automated timestamp. The officer then directs the student to the official request route and reminds them to check whether the form must be submitted before the original deadline. It is essential not to promise approval merely because a request has been lodged.
The student wonders whether uploading an empty file will protect them from a late penalty. The officer does not endorse this idea. Instead, they recommend following the published guidance and keeping a record of what was submitted and when. A helpful response gives practical steps without interpreting rules beyond the employee\'s authority. It also respects privacy: personal or medical details should be shared only through the authorised confidential channel. Clear explanations can reduce anxiety while still preserving academic fairness.''',
'''Student | My assignment is due tomorrow. Can I have an automatic extension?
Officer | I can show you the request procedure, but approval is not automatic.
Student | Do I need to apply before the deadline?
Officer | Please check the current policy. It specifies when and how requests should be submitted.
Student | Should I email my personal supporting evidence to the lecturer?
Officer | Use the university\'s approved confidential channel if the process requires evidence.
Student | What if I cannot submit by the original time?
Officer | Follow the published instructions and keep a record of the submission or request timestamp.''',
('First conditional and time clauses','Условия и сроки','Use if to state conditions and before/after/by to clarify timing. “By Friday” means no later than Friday; “until Friday” describes how long a situation continues.','If you need more time, check the policy.;Submit the form by Friday.;Please apply before the deadline.','Do not confuse “by 5 p.m.” with “after 5 p.m.”',Q('Which phrase means no later than Friday?','Submit by Friday.','Submit after Friday.','Submit from Friday.','By marks a deadline.')),
[Q('What is true about extensions in the reading?','They require the relevant procedure; approval is not automatic.','They are always granted for any reason.','Every university follows identical rules.','The officer avoids promising an outcome.'),Q('Why should students keep submission records?','To confirm what was sent and when.','To avoid opening the portal.','Because grades are set by email order.','Records support accurate follow-up.')],
[Q('Should supporting evidence always be sent to the lecturer by ordinary email?','No, use the approved confidential process.','Yes, always include private details in CC.','Send it to fellow students first.','The officer directs evidence to a secure channel.'),Q('What does the officer suggest checking?','When and how an extension request must be submitted.','Only the student’s timetable.','The café’s opening hours.','The policy specifies process and timing.')],
'Explain what a deadline means, how to request an extension and why submission does not guarantee approval.',
'A worried student asks about a deadline tomorrow. Provide calm, clear information and direct them to the correct process.',
'Please check the exact deadline in the course portal. If you need additional time, the current policy explains how to request an extension and whether evidence is required. Submitting a request does not guarantee approval. Keep your confirmation record.',
'Write a 90-word email that explains a deadline and the approved extension procedure without offering an unauthorised promise.',
'Dear Student, The published submission deadline is Friday at 17:00 local time. If you believe you need an extension, please review the assessment policy and submit the formal request through the approved portal. Check whether the request must be made before the original deadline and retain the confirmation. Any decision will be made by the authorised team. Kind regards, Academic Support',
('Please submit until 5 p.m. tomorrow.','Please submit by 5 p.m. tomorrow.','Use by to express a submission deadline.'),
Q('A student asks whether sending a request guarantees extra time. What is correct?','No; an authorised decision is still required.','Yes; submitting the form is identical to approval.','Only support officers can decide privately.','Requests and approvals are different actions.')))
LESSONS.append(make(
14,'Handling Difficult Conversations','Сложные разговоры','empathy, boundaries and de-escalation',
'''frustrated | расстроенный; раздражённый | Upset because something is not working as expected. | The student sounded frustrated about the delay.
acknowledge | признать; дать понять, что услышал | To show that you recognise someone\'s concern. | I want to acknowledge your concern.
concern | беспокойство; проблема | Something that causes worry or needs attention. | I understand your concern about the timetable.
remain calm | сохранять спокойствие | To respond without escalating emotions. | Please remain calm and focus on the next step.
professional boundary | профессиональная граница | A limit on what is appropriate in a role. | Staff must maintain professional boundaries.
de-escalate | снизить напряжение | To make a tense situation less intense. | Clear explanations can help de-escalate a conflict.
listen actively | активно слушать | To show attention and check understanding. | Listen actively before suggesting a solution.
refer to a supervisor | обратиться к руководителю | To pass a situation to a manager when appropriate. | The officer referred the issue to a supervisor.
realistic expectation | реалистичное ожидание | A result or timeframe that can reasonably be expected. | Explain a realistic expectation for the review.
follow-up plan | план дальнейших действий | Agreed steps after a conversation. | The call ended with a follow-up plan.''',
'''I understand why this is frustrating. | Я понимаю, почему это вызывает раздражение.
Thank you for explaining the situation. | Спасибо, что объяснили ситуацию.
Let me make sure I have the facts right. | Давайте я уточню факты.
Here is what I can do at this stage. | Вот что я могу сделать сейчас.
I cannot promise that outcome. | Я не могу обещать такой результат.
Would you like me to explain the next step? | Хотите, я объясню следующий шаг?''',
'A complaint about a delayed response',
'''A student arrives at the support desk visibly upset. They submitted a request several days ago and have not received a decision. Their first sentence is, “Nobody here is helping me.” The Academic Support officer has two tasks: reduce the tension and find accurate information. Arguing about the student\'s tone would probably make the situation worse. Instead, the officer acknowledges the delay and invites a concise explanation.
After listening, the officer checks the case reference and confirms that the request was forwarded to the academic team. However, the final decision is still pending. The officer explains this honestly and gives the student a realistic next step: they can request a status update through the authorised channel. They should not invent a decision date or promise approval just to end the conversation.
A difficult conversation may involve raised voices or repeated demands. Staff should remain respectful, but they are also entitled to appropriate professional boundaries and support from a supervisor. If a conversation becomes unsafe or abusive, the employee should follow workplace procedures rather than manage the situation alone. When possible, the officer ends with a short recap: what is known, what remains unknown, who will follow up and how the student will receive an update. This protects clarity and reduces the chance of a second misunderstanding.''',
'''Student | I\'ve been waiting for days. Nobody is doing anything about my request.
Officer | I\'m sorry the delay has been frustrating. Could you share your case reference so I can check the status?
Student | It\'s AS-209. I need an answer today.
Officer | Thank you. I can see the request was forwarded, but the decision is still pending.
Student | Then guarantee that it will be approved tomorrow.
Officer | I can\'t promise that outcome. What I can do is request an update from the authorised team.
Student | How will I know what happens?
Officer | We\'ll follow the approved status process and send you a clear update when information is available.''',
('Empathetic statements and limits','Эмпатия без ложных обещаний','Combine acknowledgment with factual next steps. Use “I understand…” without claiming to know another person\'s full experience. “What I can do is…” states a helpful boundary.','I understand that this is worrying.;What I can do is check the status.;I cannot guarantee a decision today.','Avoid defensive phrases such as “Calm down!” or unfounded promises.',Q('Which response combines empathy and realistic action?','I understand your concern; I can check the current status.','Calm down; this is not our problem.','I guarantee everything will be fixed immediately.','Acknowledgment plus a practical next step is most effective.')),
[Q('What is known about the delayed request?','It has been forwarded and is awaiting a decision.','It has already been approved.','It was never submitted.','The case status is pending with the authorised team.'),Q('What should happen if the conversation becomes unsafe?','Follow workplace procedures and obtain support.','Ignore all workplace safety rules.','Share the student\'s private case online.','Boundaries and appropriate escalation protect staff and students.')],
[Q('What is the student’s case reference?','AS-209.','AS-290.','AS-902.','The student provides AS-209.'),Q('Does the officer guarantee approval?','No, they offer a status check instead.','Yes, approval tomorrow.','Yes, approval immediately.','The officer avoids promises beyond their authority.')],
'Respond to an upset student with empathy, a factual status explanation and a clear follow-up route.',
'A student is angry about a delayed decision and demands certainty. Acknowledge the concern and explain what you can actually do.',
'I understand how frustrating the delay is. I have checked your case, and the decision is still pending with the authorised team. I cannot guarantee an outcome today, but I can request a status update and explain how you will be notified.',
'Write a respectful follow-up to a student who complained about slow processing. Avoid defensiveness.',
'Dear Student, Thank you for speaking with us today. I understand your concern about the delay. Your request has been forwarded to the appropriate academic team and is currently awaiting review. We cannot confirm an outcome at this stage, but we will request a status update through the approved process. Thank you for your patience. Kind regards, Academic Support',
('I understand for your frustration.','I understand your frustration.','Understand takes a direct object in this expression.'),
Q('A caller demands a guaranteed decision date you do not have. What is best?','State the uncertainty and offer a specific authorised follow-up.','Invent a date so they leave satisfied.','Argue that their frustration is unreasonable.','Honesty and next steps build credibility.')))
LESSONS.append(make(
15,'Academic Problem Solving','Решение академических проблем','structured problem solving',
'''identify the issue | определить проблему | To establish what is wrong before acting. | First, identify the issue in the registration record.
root cause | первопричина | The underlying reason a problem happened. | We need to check the root cause before changing anything.
workaround | временное решение | A temporary way to continue while a problem is investigated. | IT suggested a safe workaround for access.
resolve a case | закрыть проблему | To reach a satisfactory solution to an issue. | The case was resolved after the records were updated.
coordinate a response | согласовать ответ | To organise a joint reply across teams. | We coordinate a response with the registrar.
priority level | уровень приоритета | A category indicating how urgent an issue is. | The case was assigned a high priority level.
status update | обновление статуса | New information about progress. | The student requested a status update.
ownership | ответственность за ведение задачи | Clear accountability for following up a case. | The support team took ownership of communication.
contingency plan | запасной план | A prepared alternative if the main solution fails. | The event team prepared a contingency plan.
close the loop | довести коммуникацию до конца | To confirm that the person knows the outcome. | Remember to close the loop with the student.''',
'''Let\'s identify the main issue first. | Сначала определим основную проблему.
What have we confirmed so far? | Что мы уже подтвердили?
I\'ll coordinate with the relevant team. | Я согласую это с соответствующим отделом.
Here is a temporary workaround. | Вот временное решение.
I\'ll send a status update once we know more. | Я сообщу об изменениях, когда получим данные.
Let\'s confirm the outcome before closing the case. | Подтвердим результат, прежде чем закрывать запрос.''',
'A missing registration record on orientation day',
'''During orientation, a new student discovers that their name is not visible on a seminar attendance list. They are worried that they cannot participate, although their registration portal says the module is active. The Academic Support officer does not immediately blame the timetable team or ask the student to register again. Instead, they begin a structured investigation.
First, the officer confirms the student\'s identity through the approved process and checks the module code, registration status and class group. Second, they contact the team responsible for attendance lists to check whether the data has been refreshed. Third, they ask the seminar organiser whether there is a permitted temporary arrangement while the list is corrected. A temporary workaround must be authorised; it should not create an inaccurate official record.
Throughout the process, the officer keeps the student informed about what is known and what remains uncertain. They avoid giving repeated vague answers like “We are looking into it.” A better update names the current stage, the owner of the next action and how the student will be contacted. Finally, once the relevant team confirms the record is correct, the officer checks with the student and closes the case. Structured problem solving is not about finding an instant answer. It means gathering the facts, choosing the right owner, communicating progress and confirming the result.''',
'''Student | My module is active, but I\'m missing from today\'s attendance list. Can I join the seminar?
Officer | Let\'s check the facts first. Can you confirm the module code and class group through the approved portal?
Student | Yes. The module is RES102, Group B.
Officer | Thank you. I\'ll ask the attendance team whether the list has been updated.
Student | What should I do while they check?
Officer | I\'ll ask the seminar organiser whether a temporary arrangement is permitted. I don\'t want to guess.
Student | Will you tell me when it\'s fixed?
Officer | Yes. I\'ll send a status update and confirm the outcome before closing the case.''',
('Sequencing and cause','Последовательность решения проблемы','Use first, next, meanwhile and finally to structure problem-solving. Use because and therefore only when the causal relationship is supported by facts.','First, we verify the record.;Meanwhile, we contact the attendance team.;Finally, we confirm the corrected status.','Avoid assuming a cause before investigating evidence.',Q('Choose the clearest sequence.','First check the record; then contact the responsible team.','Finally check the record before we start.','Because the list must wrong.','Logical sequencing makes explanations usable.')),
[Q('What should the officer verify before diagnosing the problem?','Module code, registration status and group.','The student’s favourite subject.','Only the room temperature.','These details identify the precise case.'),Q('What is required of a temporary workaround?','It must be authorised and not create inaccurate records.','It should bypass all policies.','It must always be given without checking.','Workarounds should protect academic accuracy.')],
[Q('Which module and group does the student name?','RES102, Group B.','RES120, Group A.','RE102, Group C.','The dialogue provides the exact case detail.'),Q('When is the case closed?','After the corrected outcome is confirmed.','As soon as the officer sends a message.','Before any checks.','Closing the loop requires confirmation.')],
'Use a four-step problem-solving framework for a missing seminar record and communicate a factual update.',
'A student fears losing attendance credit because their name is missing from a list. Explain how you will investigate.',
'First, let\'s confirm your module code and class group. I will check the registration information and contact the team responsible for the attendance list. I will ask whether a permitted temporary arrangement is available and update you once we have confirmed the result.',
'Write a progress update that separates confirmed facts, actions in progress and the next expected contact.',
'Dear Student, We have confirmed that your registration for RES102, Group B, is active. We have contacted the attendance team to review the class list and asked the seminar organiser about any temporary arrangements. We cannot confirm the correction yet, but we will update you as soon as the responsible team provides a verified response. Kind regards, Academic Support',
('First we checking the record, then we contact the team.','First we check the record, then we contact the team.','Use Present Simple for a routine process.'),
Q('An urgent record problem appears. What should you do first?','Confirm the relevant facts before choosing an action.','Declare one team responsible without evidence.','Close the case without checking.','Accurate problem solving starts with verification.')))
