---
name: geo-seo-audit
description: GEO + SEO audit and implementation workflow — HTML structure, semantic writing, Wikipedia/Wikidata presence, structured data (JSON-LD schema), meta tags, robots.txt, sitemap, IndexNow, topic cluster architecture, performance, AI citation content patterns, platform-specific behavior, and defensive review for advocacy websites
---
# GEO + SEO Audit

Generative Engine Optimization (GEO) ensures advocacy content appears in AI answer systems: ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini, Bing Copilot. Traditional SEO remains necessary but is no longer sufficient — approximately 60% of searches end without a click.

**How AI citation works:** Google generates an answer first, then scores content against it using embedding distance. Only 17-32% of AI Overview citations come from pages ranking in the organic top 10. Domain Authority correlates with AI citations at only r=0.18; topical authority (r=0.40) and branded web mentions (r=0.664) are the real predictors. 80% of URLs cited by AI assistants do not rank in Google's top search results.

## When to Use
- When building or reviewing any public-facing advocacy website
- Before launching content that needs to be discoverable by AI systems
- When diagnosing why a site is not appearing in AI responses
- When implementing a content hub or topic cluster for an advocacy campaign
- As a pre-launch checklist for any new Open Paws platform page

## Process

### Step 1: Audit HTML Structure

Check each page for:
1. Exactly one `<h1>` tag containing the primary topic
2. Logical heading hierarchy (`h1 > h2 > h3`) with no skipped levels
3. `<h2>` headings phrased as questions where the section answers something (7× citation impact for smaller sites)
4. First paragraph after each heading: direct 40-60 word answer — AI systems pull from the first 30% of content 44% of the time
5. Paragraphs of 2-4 sentences (40-60 words); content sections of 120-180 words that make sense if extracted (70% more ChatGPT citations)
6. Semantic elements used correctly: `<article>`, `<section>`, `<nav>`, `<aside>`, `<header>`, `<footer>`, `<main>`
7. `lang` attribute on `<html>` tag
8. Descriptive `alt` text on every `<img>`
9. Meaningful anchor text on every `<a>` — never "click here"
10. `<table>` for comparison data (32.5% of AI-cited content uses tables)
11. `<ol>` and `<ul>` for lists (78% of AI answers include list formats)
12. `<blockquote cite="...">` for expert quotations (+28-40% AI visibility)
13. `<time datetime="YYYY-MM-DD">` for all dates
14. `<dfn>` for term definitions; `<abbr title="...">` for acronyms on first use
15. `id` attributes on all `<h2>` and `<h3>` elements

Flag any content rendered exclusively by JavaScript — AI crawlers often cannot execute JS.

### Step 2: Audit Semantic Writing Quality

This is a newer and underweighted audit area. AI citation systems retrieve at the sentence and paragraph level, not the page level.

**Entity salience:** Check that the primary entity appears as the grammatical subject in active voice. "Open Paws documented 34% adoption growth in 2025" (salience: 0.74) vs. "34% adoption growth was documented in 2025" (salience: 0.11). Every sentence should identify its subject explicitly.

**Atomic claims:** Verify that sentences are self-contained semantic triples (subject + verb + object with explicit context). Eliminate vague pronouns — every sentence must make sense in isolation. Vague: "It increased significantly." Citable: "Factory farm enforcement actions increased 34% between 2023 and 2025 according to USDA's annual report."

**Proper noun density:** AI-cited text averages 20.6% proper nouns versus 5-8% in standard English. Check whether the content names organizations, researchers, reports, and years specifically. Vague attribution ("experts say") never gets cited.

**Content density:** Pages under 5,000 characters get approximately 66% of their content used by AI systems; pages over 20,000 characters get only 12%. Gemini allocates roughly 380 words per webpage per query. Check whether pages are focused and dense rather than exhaustive and padded.

**Paragraph structure:** 71% of AI-cited paragraphs contain four lines or fewer. 64% include explicit feature or capability lists. Verify that every major section opens with a 40-60 word declarative answer.

### Step 3: Audit Wikipedia and Wikidata Presence

This is the highest-leverage off-site GEO action. Wikipedia accounts for 47.9% of ChatGPT's top-10 cited sources. Organizations visible in Wikidata get Google Knowledge Panels within 7 days and begin appearing consistently in AI answers.

Check:
1. Does the organization have a Wikipedia article? Is it accurate, cited, and maintained?
2. Does the organization have a Wikidata entry (Q-ID)? Is it complete with: organization type, founding date, location, founders, official website, social media profiles?
3. Is the Wikidata Q-ID referenced in the site's Organization schema `sameAs` array?
4. Is there an entity web connecting: organization → key tools/platforms → key people → related organizations → policy areas?
5. Does the site's structured data match what Wikipedia and Wikidata say? Inconsistency reduces AI confidence.
6. Does the Wikipedia article or Wikidata entry need updating to reflect the organization's current work?

If no Wikipedia page exists: document this as a **High** finding. A Wikipedia article requires reliable third-party sources — check whether sufficient coverage exists in press, academic papers, or NGO reports to support notability. If sources exist, creating the article should be prioritized over almost any on-site optimization.

### Step 4: Audit Structured Data (JSON-LD)

Sites with structured data achieve 41% AI citation rates vs 15% without. Only 12.4% of websites implement it.

For every page, verify:

**Organization + WebSite schema (required on every page):**
- `@type: Organization` with `name`, `url`, `logo`, `sameAs` (LinkedIn, Twitter, GitHub, Wikipedia URL, Wikidata URL), `description`
- `@type: WebSite` with `url`, `name`, `publisher` linking to Organization via `@id`
- Both in a `@graph` array

**Article schema (every content page):**
- `headline`, `author` (with `name`, `url`, `jobTitle`), `publisher` (via `@id`), `datePublished`, `dateModified`, `image`, `description`

**FAQPage schema (any page with Q&A content):**
- Each question: `@type: Question` with `name` and `acceptedAnswer.text` (40-80 word direct answer)

**Also implement when applicable:** HowTo, BreadcrumbList, SoftwareApplication, Event, Dataset, Person.

Validate all schema at schema.org/validator and Google's Rich Results Test. `dateModified` must reflect actual update dates — never fake it.

### Step 5: Audit Meta Tags and Head Elements

For every page:
- `<title>`: `Primary Keyword — Brand Name`, 50-60 chars, keywords first, unique per page
- `<meta name="description">`: 150-160 chars, direct factual answer to the primary query, one specific statistic, unique per page
- `<link rel="canonical">` pointing to the canonical URL
- Open Graph tags: `og:title`, `og:description`, `og:type`, `og:url`, `og:image`, `og:site_name`
- Twitter Card tags: `twitter:card` (summary_large_image), `twitter:title`, `twitter:description`, `twitter:image`
- Article timestamps: `article:published_time`, `article:modified_time` (ISO 8601)

### Step 6: Audit Robots.txt

Verify the site allows AI citation crawlers:

**Must allow (these power AI answers):**
- `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `ClaudeBot`, `Claude-SearchBot`, `Applebot`, `Amazonbot`

**May optionally block (training, not answers):**
- `GPTBot`, `CCBot`, `Google-Extended`, `meta-externalagent`, `Bytespider`

Note: blocking `Googlebot` blocks both Google Search AND Google AI Overviews. There are now 226+ identified AI crawlers — verify the list is current. Some AI agents use standard browser user-agent strings and ignore robots.txt entirely; treat this as best-effort control.

### Step 7: Audit XML Sitemap

- Exists at `/sitemap.xml`
- Contains only canonical, indexable URLs
- `<lastmod>` dates reflect actual content update dates
- Sitemap referenced in robots.txt
- Submitted to Google Search Console and Bing Webmaster Tools
- Auto-regenerates when content changes

### Step 8: Audit IndexNow Integration

IndexNow notifies Bing (which feeds ChatGPT) instantly when content changes. Check:
1. API key file exists at `https://yoursite.com/{key}.txt`
2. Ping fires on every publish/update event
3. Integration is in CI/CD pipeline or CMS publish hooks

### Step 9: Audit Site Architecture and Content Freshness

URLs: descriptive hyphenated lowercase, under 75 characters, max 3 levels deep, canonical tags on every page, 301 redirects for URL changes.

Topic cluster architecture (citation rate 12% → 41%):
- Is there a pillar page (2,000-4,000 words) for each major advocacy topic?
- Does each pillar have 8-15 cluster pages on specific subtopics?
- Are all links bidirectional?
- Are cluster pages siloed from each other, or is content fragmented?

Content freshness:
- "Last Updated: [date]" visible on every content page using `<time datetime="YYYY-MM-DD">`
- `dateModified` in Article schema synchronized with visible dates
- 76% of most-cited AI content was updated within 30 days; Perplexity gives 3.4× advantage to content under 30 days old

**First-mover check:** For emerging topics in the advocacy space with few authoritative sources, verify the site is publishing content before competitors claim those citation positions.

### Step 10: Audit Platform Presence and Cross-Platform Consistency

85% of AI brand mentions come from third-party pages. Check:
1. **Reddit:** Active, authentic participation in relevant subreddits? Note: AI systems have visibility into Reddit's moderation pipeline — inauthentic content carries negative weight.
2. **YouTube:** Channel exists with transcripts enabled? Transcripts are crawlable text.
3. **LinkedIn:** Organization page active with substantive posts?
4. **GitHub:** Documentation, datasets, or reports published as Markdown?
5. **Authoritative databases:** Data submitted to Our World in Data, government data portals, or relevant academic databases?

Cross-platform consistency: verify that key factual claims (founding date, mission statement, key statistics) are consistent across the site, Wikipedia, Wikidata, LinkedIn, and GitHub. Inconsistency reduces AI confidence in citations.

Platform-specific behavior: only 11% of domains are cited by both ChatGPT and Perplexity for the same queries — each platform has different citation patterns. Citation volatility is extreme: 40-60% monthly turnover is normal. Build multi-platform presence rather than optimizing for any single system.

### Step 11: Audit Performance

AI crawlers timeout at 1-5 seconds:
- TTFB < 200ms
- LCP < 2.5s
- CLS < 0.1
- Total page weight < 1MB (18% of pages over 1MB are abandoned by AI crawlers)

Verify: SSR or SSG, gzip or brotli, modern image formats (WebP/AVIF), HTTPS, mobile-responsive.

### Step 12: Audit Content Patterns

Check whether content templates implement high-citation patterns:

**Citable paragraph:** every major claim follows `[fact]. [statistic with attribution]. [elaboration]. [Source: Org, Date]`

**FAQ block:** `<h2>` with exact question, 40-60 word direct answer immediately following, FAQPage schema.

**Definition block:** `<section id="what-is-term"><h2>What is [Term]?</h2><p><dfn>[Term]</dfn> is [direct definition]...</p></section>`

**Author attribution:** visible name, credentials, profile page link, Person schema. +40% citations.

**Proprietary data:** pages with original data or research get 4.31× more citations per URL. Check whether any unique datasets, survey results, or original research can be published as dedicated pages.

### Step 13: Defensive Review

Check for techniques that would violate platform guidelines and expose the site to penalties:

**Hidden text:** verify no content is hidden via `display:none`, `visibility:hidden`, white-on-white text, zero-size fonts, or negative positioning. Google's SpamBrain and detection tools like PhantomLint compare parsed text against OCR-rendered images. Penalties are domain-wide.

**Agent-aware cloaking:** verify the server does not serve different content to AI crawlers vs human visitors based on User-Agent detection. This is explicitly prohibited by all major platforms and carries domain-wide penalty risk.

**Scaled AI content:** verify all published content has meaningful human review. The March 2024 Google core update caused sites relying on scaled AI content to lose up to 80% of organic traffic overnight.

**Injection risk in user-generated content:** if the site hosts comments, forum posts, or user submissions, verify they are sanitized before being served to crawlers. Third-party injection into UGC is an emerging attack vector.

### Step 14: Findings Report

Document findings by priority:

**Critical (blocks launch)**
- Primary content rendered JavaScript-only
- Missing `<h1>` or broken heading hierarchy
- Missing canonical tags
- robots.txt blocking AI citation crawlers
- Missing HTTPS
- Agent-aware cloaking detected

**High (implement before significant content investment)**
- No Wikipedia article when sufficient notability sources exist
- No Wikidata entry
- Missing structured data (JSON-LD schema)
- Content siloed with no topic cluster architecture
- Pages not SSR or SSG
- LCP > 2.5s or page weight > 1MB
- `sameAs` links missing Wikipedia/Wikidata URLs

**Medium (implement in next sprint)**
- Question-format headings not used
- Answer-first paragraph pattern not followed
- Missing entity salience (passive voice, vague pronouns)
- Content density outside optimal range
- Missing author attribution
- Missing IndexNow integration
- Outdated or missing `dateModified` values
- No Reddit or YouTube presence
- Key facts inconsistent across platforms

**Low (optimize over time)**
- llms.txt not implemented (low current value but zero-cost)
- Individual content not following citable paragraph pattern
- Missing comparison tables on decision-relevant pages
- No proprietary data or original research pages
- GitHub presence not established

For each finding: the specific page or component affected, what is missing or incorrect, and the exact implementation needed.
