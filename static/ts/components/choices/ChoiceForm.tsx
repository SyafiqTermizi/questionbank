import * as React from "react";
import { useState } from "react";

import { IChoice } from "../interfaces";
import { CardLayout } from "../../layouts/CardLayout";
import { editorConfig } from "./editorConfig";

const Editor = require("ckeditor4-react");

interface Props {
  choices: IChoice[],
  setChoices: (args: IChoice[]) => void;
}

export const ChoiceForm: React.FC<Props> = ({ choices, setChoices }) => {
  const defaultChoice = {
    text: "",
    isCorrect: false,
    id: Date.now()
  }
  const [choice, setChoice] = useState(defaultChoice);

  return (
    <CardLayout cardTitle="Answer options">
      <form onSubmit={
        (event) => {
          event.preventDefault();
          if (choice.text) {
            setChoices([...choices, choice]);
            setChoice(defaultChoice);
          }
        }}
      >
        <div className="form-group">
          <Editor
            data={choice.text}
            config={editorConfig}
            onChange={(event: any) => {
              setChoice({ ...choice, text: event.editor.getData()});
            }}
          />
        </div>
        <div className="form-check">
          <label className="form-check-label" htmlFor="isCorrect">
            <input
              className="form-check-input"
              type="checkbox"
              id="isCorrect"
              checked={choice.isCorrect}
              onChange={() => {
                const tempIsCorrect = choice.isCorrect;
                setChoice({...choice, isCorrect: !tempIsCorrect})
              }}
            />
            Correct answer
          </label>
        </div>
        <div className="form-group mt-3">
          <input type="submit" value="Add Choice" className="btn btn-primary"/>
        </div>
      </form>
    </CardLayout>
  )
}
