// ESLint flat config for no-animal-violence plugin
// For projects using ESLint v9+ flat config
import noAnimalViolence from "eslint-plugin-no-animal-violence";

export default [
  {
    plugins: {
      "no-animal-violence": noAnimalViolence,
    },
    rules: {
      "no-animal-violence/no-violent-language": "error",
    },
  },
];
