"use strict";

const rules = require("./rules/no-violent-language");

module.exports = {
  rules: {
    "no-speciesist-language": rules,
  },
  configs: {
    recommended: {
      plugins: ["speciesism"],
      rules: {
        "speciesism/no-speciesist-language": "warn",
      },
    },
  },
};
