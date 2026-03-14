// AUTO-GENERATED from project-compassionate-code. Do not edit directly.
"use strict";

/**
 * Map of animal violence phrases to their inclusive alternatives.
 * Keys are lowercase for case-insensitive matching.
 */
const VIOLENT_ANIMAL_PHRASES = new Map([
  ["kill two birds with one stone", "accomplish two things at once"],
  ["beat a dead horse", "belabor the point"],
  ["more than one way to skin a cat", "more than one way to solve this"],
  ["let the cat out of the bag", "reveal the secret"],
  ["open a can of worms", "create a complicated situation"],
  ["wild goose chase", "futile search"],
  ["like shooting fish in a barrel", "trivially easy"],
  ["flog a dead horse", "belabor the point"],
  ["there are bigger fish to fry", "more important matters to address"],
  ["guinea pig", "test subject"],
  ["hold your horses", "wait a moment"],
  ["the elephant in the room", "the obvious issue"],
  ["straight from the horse's mouth", "directly from the source"],
  ["bring home the bacon", "bring home the results"],
  ["take the bull by the horns", "face the challenge head-on"],
  ["like lambs to the slaughter", "without resistance"],
  ["no room to swing a cat", "very cramped"],
  ["red herring", "distraction"],
  ["curiosity killed the cat", "curiosity backfired"],
  ["like a chicken with its head cut off", "in a panic"],
  ["your goose is cooked", "you're in trouble"],
  ["throw someone to the wolves", "abandon to criticism"],
  ["hook, line, and sinker", "completely"],
  ["clip someone's wings", "restrict someone's freedom"],
  ["the straw that broke the camel's back", "the tipping point"],
  ["a bird in the hand is worth two in the bush", "a sure thing beats a possibility"],
  ["eat crow", "admit being wrong"],
  ["fight like cats and dogs", "constantly argue"],
  ["take the bait", "fall for it"],
  ["don't count your chickens before they hatch", "don't assume success prematurely"],
  ["don't be a chicken", "don't hesitate"],
  ["pig", "resource-intensive"],
  ["cowboy coding", "undisciplined coding"],
  ["code monkey", "developer"],
  ["badger someone", "pester"],
  ["ferret out", "uncover"],
  ["cattle vs. pets", "ephemeral vs. persistent"],
  ["pet project", "side project"],
  ["canary in a coal mine", "early warning signal"],
  ["dogfooding", "self-hosting"],
  ["herding cats", "coordinating independent contributors"],
  ["go on a fishing expedition", "exploratory investigation"],
  ["sacred cow", "unquestioned belief"],
  ["scapegoat", "blame target"],
  ["rat race", "daily grind"],
  ["dead cat bounce", "temporary rebound"],
  ["dog-eat-dog", "ruthlessly competitive"],
  ["whack-a-mole", "recurring problem"],
  ["cash cow", "profit center"],
  ["sacrificial lamb", "expendable person"],
  ["sitting duck", "easy target"],
  ["open season", "free-for-all"],
  ["put out to pasture", "retire"],
  ["dead duck", "lost cause"],
  ["kill process", "terminate the process"],
  ["kill the server", "stop the server"],
  ["nuke", "delete completely"],
  ["abort", "cancel"],
  ["cull", "remove"],
  ["master/slave", "primary/replica"],
  ["whitelist/blacklist", "allowlist/denylist"],
  ["grandfathered", "legacy"],
]);

/**
 * Build a combined regex that matches any of the violent animal phrases.
 * Uses word boundaries where appropriate and is case-insensitive.
 */
function buildPattern() {
  const escaped = Array.from(VIOLENT_ANIMAL_PHRASES.keys()).map((phrase) =>
    phrase.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
  );
  // Sort longest-first so longer phrases match before shorter substrings
  escaped.sort((a, b) => b.length - a.length);
  return new RegExp(`\\b(?:${escaped.join("|")})\\b`, "gi");
}

const PATTERN = buildPattern();

/**
 * Check a string for violent animal phrases and report any matches.
 */
function checkText(context, node, text, offsetCalculator) {
  PATTERN.lastIndex = 0;
  let match;
  while ((match = PATTERN.exec(text)) !== null) {
    const phrase = match[0].toLowerCase();
    const alternative = VIOLENT_ANIMAL_PHRASES.get(phrase);
    if (alternative) {
      const loc = offsetCalculator
        ? offsetCalculator(match.index)
        : node.loc.start;

      context.report({
        node,
        loc,
        messageId: "avoidViolentAnimalLanguage",
        data: {
          phrase: match[0],
          alternatives: alternative,
        },
      });
    }
  }
}

module.exports = {
  meta: {
    type: "suggestion",
    docs: {
      description: "Detect and discourage language normalizing violence toward animals in comments and strings",
      category: "Best Practices",
      recommended: true,
      url: "https://github.com/Open-Paws/eslint-plugin-no-animal-violence#no-violent-language",
    },
    messages: {
      avoidViolentAnimalLanguage:
        'Avoid "{{phrase}}". Consider: {{alternatives}}',
    },
    schema: [],
  },

  create(context) {
    const sourceCode = context.getSourceCode
      ? context.getSourceCode()
      : context.sourceCode;

    return {
      // Check string literals
      Literal(node) {
        if (typeof node.value === "string") {
          checkText(context, node, node.value);
        }
      },

      // Check template literal quasi elements
      TemplateLiteral(node) {
        node.quasis.forEach((quasi) => {
          checkText(context, quasi, quasi.value.raw);
        });
      },

      // Check all comments when the program node is visited
      Program() {
        const comments = sourceCode.getAllComments
          ? sourceCode.getAllComments()
          : (sourceCode.comments || []);

        comments.forEach((comment) => {
          checkText(context, comment, comment.value, (matchIndex) => {
            // Calculate approximate location within the comment
            const lines = comment.value.substring(0, matchIndex).split("\n");
            const lineOffset = lines.length - 1;
            const columnOffset =
              lineOffset === 0
                ? matchIndex + (comment.type === "Block" ? 2 : 2)
                : lines[lines.length - 1].length;

            return {
              line: comment.loc.start.line + lineOffset,
              column:
                lineOffset === 0
                  ? comment.loc.start.column + columnOffset
                  : columnOffset,
            };
          });
        });
      },
    };
  },
};
