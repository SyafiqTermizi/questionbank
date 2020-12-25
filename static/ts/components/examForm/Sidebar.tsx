import * as React from "react";
import { useEffect, useState } from "react";
import axios from "axios";

export const Sidebar = () => {
  const [topics, setTopics] = useState([]);
  const [tags, setTags] = useState([]);

  useEffect(() => {
    const courseId = window.location.pathname.match(/[0-9]+/)[0];
    axios.get(`/questions/api/topics/?exam_id=${courseId}`)
      .then(res => setTopics(res.data))

    axios.get(`/questions/api/tags/?exam_id=${courseId}`)
      .then(res => setTags(res.data))

  }, [])

  return (
    <div className="row">
      <div className="col-12">
        <div className="card">
          <div className="card-header">
            <b>Filter</b>
          </div>
          <div className="card-body">
            <h6>Topics</h6>
            {topics.map(
              topic => (
                <span key={topic}>
                  <a className="badge badge-secondary">{topic}</a>
                  <br/>
                </span>
              )
            )}
          </div>
          <div className="card-body">
            <hr/>
            <h6>Tags</h6>
            {tags.map(
              tag => (
                <span key={tag.tag_id}>
                  <a className="badge badge-secondary">{tag.name}</a>
                  <br/>
                </span>
              )
            )}
          </div>
        </div>
      </div>
    </div>
  )
}
