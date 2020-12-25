import * as React from "react";
import { useEffect, useState } from "react";
import axios from "axios";

export const QuestionList = () => {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    const courseId = window.location.pathname.match(/[0-9]+/)[0];

    axios.get(`/questions/api/questions/?exam_id=${courseId}`)
      .then(res => setQuestions(res.data))
  })

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
