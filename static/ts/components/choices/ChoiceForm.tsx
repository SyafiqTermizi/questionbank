import * as React from "react";
import { useState } from "react";

import { IChoice } from "../interfaces";
import { CardLayout } from "../../layouts/CardLayout";

interface Props {
  choices: IChoice[],
  setChoices: (args: IChoice[]) => void;
}

export const ChoiceForm: React.FC<Props> = ({ choices, setChoices }) => {
  const defaultChoice = {
    text: "",
    isCorrect: false
  }
  const [choice, setChoice] = useState(defaultChoice);

  return (
    <CardLayout cardHeaderTitle="Create Choice">
      <form onSubmit={
        (event) => {
          event.preventDefault();
          setChoices([...choices, choice]);
          setChoice(defaultChoice);
        }}
      >
        <div className="form-group">
          <textarea
            className="form-control"
            cols={30}
            rows={10}
            value={choice.text}
            onChange={(event) => {
              setChoice({ ...choice, text: event.target.value});
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
            Is correct
          </label>
        </div>
        <div className="form-group mt-3">
          <input type="submit" value="Add Choice" className="btn btn-primary"/>
        </div>
      </form>
    </CardLayout>
  )
}
