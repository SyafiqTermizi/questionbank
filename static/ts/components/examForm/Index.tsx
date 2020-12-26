import * as React from "react";
import * as ReactDom from "react-dom";
import { useEffect, useState } from "react";
import axios from "axios";

import { Sidebar } from "./Sidebar";
import { QuestionList } from "./QuestionList";


export const ExamForm = () => {
  const apiFetcher = axios.create({
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFTOKEN",
  });

  const BASE_API = "/questions/api/";
  const examId = window.location.pathname.match(/[0-9]+/)[0];

  const [questions, setQuestions] = useState([]);
  const [topics, setTopics] = useState([]);
  const [tags, setTags] = useState([]);
  const [topicFilter, setTopicFilter] = useState("");
  const [tagFilter, setTagFilter] = useState("");

  const setCurrentTopic = (topic: string): void => {
    const newTopicFilter = topic === topicFilter ? "" : topic;
    setTopicFilter(newTopicFilter);
  }

  const setCurrentTag = (tag: string): void => {
    const newTagFilter = tag === tagFilter ? "" : tag;
    setTagFilter(newTagFilter);
  }

  const fetchQuestions = (): void => {
    apiFetcher.get(`${BASE_API}questions/?exam_id=${examId}&topic=${topicFilter}&tags__id=${tagFilter}`)
      .then(res => setQuestions(res.data))
  }

  const addQuestion = (questionId: number): void => {
    apiFetcher.post(`/exams/api/add-question/${examId}/?question_id=${questionId}`)
      .then(() => fetchQuestions())
  }

  useEffect(() => {
    apiFetcher.get(`${BASE_API}topics/?exam_id=${examId}`)
      .then(res => setTopics(res.data))

    apiFetcher.get(`${BASE_API}tags/?exam_id=${examId}`)
      .then(res => setTags(res.data))
  }, [])

  useEffect(() => {
    fetchQuestions()
  }, [topicFilter, tagFilter])

  return (
    <div className="row mt-3">
      <div className="col-2">
        <Sidebar
          topics={topics}
          tags={tags}
          topicFilter={topicFilter}
          tagFilter={tagFilter}
          setTopicFilter={setCurrentTopic}
          setTagFilter={setCurrentTag}
        />
      </div>
      <div className="col-10">
        <QuestionList questions={questions} addToExam={addQuestion} />
      </div>
    </div>
  )
};

ReactDom.render(
  <ExamForm />,
  document.getElementById("exam-form")
)
