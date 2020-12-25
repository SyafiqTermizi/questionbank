import * as React from "react";

interface Question {
  id: number;
  created_by: string;
  created_at: string;
  question: string;
  choices: string;
}

interface Props {
  questions: Question[];
}

export const QuestionList: React.FC<Props> = ({ questions }) => {

  const questionsComp = questions.map(question => (
    <div key={question.id} className="card mt-3">
      <div className="card-header">
        <div className="row">
          <div className="col-6">
            <b>{question.created_by} | {question.created_at}</b>
          </div>
        </div>
      </div>
      <div className="card-body">
        <span dangerouslySetInnerHTML={{__html: question.question}}></span>
        <br/>
        <span dangerouslySetInnerHTML={{__html: question.choices}}></span>
      </div>
    </div>
  ))

  return <>{questionsComp}</>
}
