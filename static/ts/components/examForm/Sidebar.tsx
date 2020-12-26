import * as React from "react";

interface Tag {
  name: string;
  tag_id: string;
}

interface Props {
  topics: string[];
  tags: Tag[];
  topicFilter: string;
  tagFilter: string;
  setTagFilter: (tagId: string) => void;
  setTopicFilter: (topic: string) => void;
}

export const Sidebar: React.FC<Props> = ({
  topics,
  tags,
  topicFilter,
  tagFilter,
  setTopicFilter,
  setTagFilter
}) => (
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
                <a
                  href="#"
                  className={`badge badge-${topicFilter == topic ? "info":"secondary" }`}
                  onClick={() => setTopicFilter(topic)}
                >
                  {topic}
                </a>
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
                <a
                  href="#"
                  className={`badge badge-${tagFilter == tag.tag_id ? "info":"secondary" }`}
                  onClick={() => setTagFilter(tag.tag_id)}
                >
                  {tag.name}
                </a>
                <br/>
              </span>
            )
          )}
        </div>
      </div>
    </div>
  </div>
)
