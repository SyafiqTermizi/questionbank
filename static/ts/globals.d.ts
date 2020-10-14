export {}

export interface IChoice {
  isCorrect: boolean;
  text: string;
  id: number;
}

declare global {
  interface Window {
    choices: IChoice[];
  }
}
