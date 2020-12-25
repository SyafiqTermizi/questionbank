import * as React from "react";
import * as ReactDom from "react-dom";
import { useEffect, useState } from "react";
import axios from "axios";

import { Sidebar } from "./Sidebar";
import { QuestionList } from "./QuestionList";


export const ExamForm = () => {
  const BASE_API = "/questions/api/";
  const courseId = window.location.pathname.match(/[0-9]+/)[0];

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

  useEffect(() => {
    axios.get(`${BASE_API}topics/?exam_id=${courseId}`)
      .then(res => setTopics(res.data))

    axios.get(`${BASE_API}tags/?exam_id=${courseId}`)
      .then(res => setTags(res.data))
  }, [])

  useEffect(() => {
    axios.get(`${BASE_API}questions/?exam_id=${courseId}&topic=${topicFilter}&tags__id=${tagFilter}`)
      .then(res => setQuestions(res.data))
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
        <QuestionList questions={questions} />
      </div>
    </div>
  )
};

ReactDom.render(
  <ExamForm />,
  document.getElementById("exam-form")
)
