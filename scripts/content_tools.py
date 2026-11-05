"""Authoring helpers. All academic situations are fictional and institution-neutral."""
from __future__ import annotations
from typing import Any

def lesson(day: int, title: str, title_ru: str, focus: str, objectives: str, vocab: str,
           phrases: str, reading_title: str, reading: str, dialogue: str,
           grammar_title: str, grammar_ru: str, grammar_rule: str, grammar_examples: str,
           grammar_trap: str, reading_q: list, listening_q: list,
           grammar_q: tuple, challenge: str, speaking: str, sample: str,
           rubric: str, writing: str, writing_sample: str,
           error: tuple, situation: tuple) -> dict[str, Any]:
    """Vocabulary row: term | Russian translation | English definition | example.
       Phrase row: English | Russian translation.
       Dialogue row: speaker | utterance.
       Question tuple: (question, [option1, option2, option3], correct_index, explanation).
    """
    def parse_rows(raw, count):
        rows = []
        for line in raw.strip().splitlines():
            if not line.strip(): continue
            fields = [x.strip() for x in line.split(' | ')]
            if len(fields) != count: raise ValueError(f'day {day}: {count} parts required, got {len(fields)}: {line}')
            rows.append(fields)
        return rows
    entries = parse_rows(vocab, 4)
    p_entries = parse_rows(phrases, 2)
    d_entries = parse_rows(dialogue, 2)
    return {
        'day': day, 'id': f'day-{day:02d}', 'title': title, 'titleRu': title_ru,
        'focus': focus, 'objectives': [x.strip() for x in objectives.split(';')],
        'vocab': [{'id':f'w{day:02d}-{i:02d}', 'term':e[0], 'ru':e[1], 'definition':e[2], 'example':e[3], 'level':'B1+' if day<16 else 'B1–B2'} for i,e in enumerate(entries, 1)],
        'phrases': [{'en':p[0], 'ru':p[1]} for p in p_entries],
        'reading': {'title':reading_title, 'text':reading.strip()},
        'dialogue': {'title':f'{title} · workplace audio', 'lines':[{'speaker':d[0], 'text':d[1]} for d in d_entries]},
        'grammar': {'title':grammar_title, 'ru':grammar_ru, 'rule':grammar_rule,
                   'examples':[x.strip() for x in grammar_examples.split(';')], 'trap': grammar_trap},
        'readingChecks':[{'q':q, 'options':o, 'answer':a, 'explanation':ex} for q,o,a,ex in reading_q],
        'listeningChecks':[{'q':q, 'options':o, 'answer':a, 'explanation':ex} for q,o,a,ex in listening_q],
        'grammarCheck':{'q':grammar_q[0],'options':grammar_q[1],'answer':grammar_q[2],'explanation':grammar_q[3]},
        'errorCorrection':{'incorrect':error[0],'correct':error[1],'explanation':error[2]},
        'situational':{'q':situation[0], 'options':situation[1], 'answer':situation[2], 'explanation':situation[3]},
        'challenge': challenge,
        'speaking':{'prompt':speaking,'sample':sample,'criteria':[x.strip() for x in rubric.split(';')]},
        'writing':{'prompt':writing,'sample':writing_sample,'criteria':['Clear purpose and relevant facts','Appropriate professional tone','Actionable next step','Accurate, readable English']}
    }
