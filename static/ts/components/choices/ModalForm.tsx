import React from "react";
import { useState, useEffect } from "react";

import { IChoice } from "../interfaces";
import { ModalLayout } from "../../layouts/ModalLayout";

import { editorConfig } from "./editorConfig";

const Editor = require("ckeditor4-react");

interface Props {
  choice: IChoice;
  choices: IChoice[];
  setChoices: (arg: IChoice[]) => void;
}

export const ModalForm: React.FC<Props> = ({ choice, choices, setChoices }) => {
  const [localChoice, setLocalChoice] = useState<IChoice>({
    text: "",
    isCorrect: false,
    id: 0,
  });

  useEffect(() => {
    const tempChoice = { ...choice };
    setLocalChoice(tempChoice);
  }, [choice]);

  const submit = () => {
    const index = choices.indexOf(choice);
    const tempChoices = [...choices];
    tempChoices[index] = localChoice;
    setChoices(tempChoices);
  };

  return (
    <ModalLayout headerText="Update">
      {localChoice.id && (
        <form>
          <div className="modal-body">
            <Editor
              data={localChoice.text}
              config={editorConfig}
              onChange={(event: any) => {
                setLocalChoice({
                  ...localChoice,
                  text: event.editor.getData(),
                });
              }}
            />
            <div className="form-check">
              <input
                className="form-check-input"
                type="checkbox"
                checked={localChoice.isCorrect}
                onChange={() =>
                  setLocalChoice({
                    ...localChoice,
                    isCorrect: !localChoice.isCorrect,
                  })
                }
                id="isCorrectModal"
              />
              <label className="form-check-label" htmlFor="isCorrectModal">
                Correct Answer
              </label>
            </div>
          </div>
          <div className="modal-footer">
            <button
              type="button"
              className="btn btn-secondary"
              data-dismiss="modal"
            >
              Close
            </button>
            <button
              type="button"
              className="btn btn-primary"
              data-dismiss="modal"
              onClick={() => submit()}
            >
              Save changes
            </button>
          </div>
        </form>
      )}
    </ModalLayout>
  );
};
