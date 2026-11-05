from content_tools import lesson

def Q(question, correct, wrong1, wrong2, explanation):
    return (question, [correct,wrong1,wrong2],0,explanation)

def make(day, title, ru, focus, vocab, phrases, reading_title, reading, dialogue, grammar,
         rq, lq, challenge, speaking, model, writing, writing_sample, error, situation,
         objectives=None, rubric=None):
    # grammar: (title, russian_caption, rule, examples_semicolon, common_mistake, Q tuple)
    if objectives is None:
        objectives = f'Understand the key terminology for {focus};Explain a relevant procedure or situation clearly;Respond appropriately in a realistic workplace conversation;Produce a short professional spoken or written response'
    if rubric is None:
        rubric = 'Address the actual request;Include the relevant facts or next steps;Use polite, natural professional English;Avoid promises beyond your authority'
    def rotate(q, i):
        text,opts,idx,expl=q
        shift=(day+i)%3
        return (text, opts[shift:]+opts[:shift], (idx-shift)%3, expl)
    return lesson(day,title,ru,focus,objectives,vocab,phrases,reading_title,reading,dialogue,
                  grammar[0], grammar[1], grammar[2],grammar[3],grammar[4],
                  [rotate(q,i) for i,q in enumerate(rq)], [rotate(q,i+1) for i,q in enumerate(lq)],
                  rotate(grammar[5],3),challenge,speaking,model,rubric,writing,writing_sample,
                  error,rotate(situation,4))
