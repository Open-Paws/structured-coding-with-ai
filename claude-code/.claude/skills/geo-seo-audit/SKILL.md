---
name: geo-seo-audit
description: GEO + SEO audit and implementation workflow — HTML structure, structured data (JSON-LD schema), meta tags, robots.txt, sitemap, IndexNow, topic cluster architecture, performance, and AI citation patterns for advocacy websites
---
# GEO + SEO Audit

Generative Engine Optimization (GEO) ensures advocacy content appears in AI answer systems: ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini, Bing Copilot. Traditional SEO remains necessary but is no longer sufficient — approximately 60% of searches end without a click. AI citation rates increase 40-115% when content follows specific structural patterns. This skill audits an existing site or guides implementation of a new one.

## When to Use
- When building or reviewing any public-facing advocacy website
- Before launching content that needs to be discoverable by AI systems
- When diagnosing why a site is not appearing in AI responses
- When implementing a content hub or topic cluster for an advocacy campaign
- As a pre-launch checklist for any new Open Paws platform page or external-facing tool

## Process

### Step 1: Audit HTML Structure

Check each page for:

1. Exactly one `<h1>` tag containing the primary topic
2. Logical heading hierarchy (`h1 > h2 > h3`) with no skipped levels
3. `<h2>` headings phrased as questions where the section answers something (7× citation impact)
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
15. `id` attributes on all `<h2>` and `<h3>` elements for deep linking

Flag any content that is rendered exclusively by JavaScript. AI crawlers often cannot execute JS — all primary content must be in the initial HTML response (SSR or pre-rendered).

### Step 2: Audit Structured Data (JSON-LD)

Structured data is the single highest-leverage GEO action: 41% citation rate with schema vs 15% without. Only 12.4% of websites implement it — a major competitive advantage.

For every page, verify the following schema exists and is valid:

**Organization + WebSite schema (required on every page):**
- `@type: Organization` with `name`, `url`, `logo`, `sameAs` (LinkedIn, Twitter, GitHub, Wikipedia), `description`
- `@type: WebSite` with `url`, `name`, `publisher` linking to Organization via `@id`
- Both in a `@graph` array under `@context: https://schema.org`

**Article schema (every content page):**
- `headline`, `author` (with `name`, `url`, `jobTitle`), `publisher` (via `@id`), `datePublished`, `dateModified`, `image`, `description`
- Author links to an author profile page with Person schema

**FAQPage schema (any page with Q&A content):**
- Each question uses `@type: Question` with `name` (exact question text) and `acceptedAnswer.text` (40-80 word direct answer)

**Also implement when applicable:**
- `HowTo` — instructional/tutorial content
- `BreadcrumbList` — navigation hierarchy
- `SoftwareApplication` — tools/platforms
- `Event` — hackathons, programs, webinars
- `Dataset` — published research data
- `Person` — team and author profiles

Validate all schema at schema.org/validator and Google's Rich Results Test. Every `sameAs` URL must resolve to a live, accurate profile. `dateModified` must reflect actual update dates — never fake it.

### Step 3: Audit Meta Tags and Head Elements

For every page verify:
- `<title>` tag: `Primary Keyword — Brand Name`, 50-60 chars, keywords first, unique per page
- `<meta name="description">`: 150-160 chars, direct factual answer to the primary query, one specific statistic, unique per page
- `<link rel="canonical">` pointing to the canonical URL
- Open Graph tags: `og:title`, `og:description`, `og:type`, `og:url`, `og:image`, `og:site_name`
- Twitter Card tags: `twitter:card` (summary_large_image), `twitter:title`, `twitter:description`, `twitter:image`
- Article timestamps: `article:published_time`, `article:modified_time` (ISO 8601 format)

### Step 4: Audit robots.txt

Verify the site allows AI citation crawlers while controlling training crawlers:

AI search and citation crawlers that should be **allowed** (these power AI answers):
- `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `ClaudeBot`, `Claude-SearchBot`, `Applebot`, `Amazonbot`

AI training crawlers that may optionally be **blocked** (these train models, not answer them):
- `GPTBot`, `CCBot`, `Google-Extended`, `meta-externalagent`, `Bytespider`

Standard search bots to allow: `Googlebot`, `Bingbot`

Note: blocking `Googlebot` blocks both Google Search AND Google AI Overviews — there is no way to separate them. Advise the project owner before blocking Googlebot.

Verify `Sitemap:` directive points to the sitemap URL.

### Step 5: Audit XML Sitemap

Check:
- Sitemap exists at `/sitemap.xml`
- Contains only canonical, indexable URLs (no redirects, no `noindex` pages)
- `<lastmod>` dates reflect actual content update dates — not faked
- Sitemap referenced in robots.txt
- Submitted to Google Search Console and Bing Webmaster Tools
- Regenerates automatically when content changes
- Under 50,000 URLs and 50MB uncompressed per file

### Step 6: Implement IndexNow (Bing/ChatGPT Discovery)

IndexNow notifies Bing (which feeds ChatGPT) instantly when content is published or updated. Dramatically accelerates AI discovery.

Check whether IndexNow is integrated:
1. API key file at `https://yoursite.com/{key}.txt` containing only the key
2. Ping on every publish: `GET https://api.indexnow.org/indexnow?url=<page-url>&key=<key>`
3. Or batch POST to `https://api.indexnow.org/indexnow` with `host`, `key`, `urlList`
4. Integration into CI/CD pipeline or CMS publish hooks

IndexNow is supported by Bing, Yandex, Seznam, Naver. It does not affect Google (use Search Console API for Google). Rate limit: 10,000 URLs/day.

### Step 7: Audit Site Architecture

URL structure:
- Descriptive, hyphenated, lowercase URLs under 75 characters
- Primary keyword in the URL
- Maximum 3 levels deep
- Canonical tags on every page
- 301 redirects for any URL changes

Navigation:
- No important page more than 3 clicks from homepage
- Breadcrumb navigation with BreadcrumbList schema

Topic cluster architecture (increases citation rate from 12% to 41%):
- Identify pillar topics relevant to the advocacy mission
- **Pillar page**: 2,000-4,000 words on the broad topic, targeting head keywords
- **Cluster pages**: 8-15 detailed pages each targeting a specific subtopic
- **Bidirectional linking**: every cluster page links to the pillar; the pillar links to every cluster page
- Assess whether the current site has this structure or if content is isolated/siloed

Content freshness:
- "Last Updated: [date]" visible on every content page using `<time datetime="YYYY-MM-DD">`
- `dateModified` in Article schema synchronized with visible dates
- 76% of the most-cited AI content was updated within 30 days

### Step 8: Audit Performance

AI crawlers timeout at 1-5 seconds:
- TTFB < 200ms
- LCP < 2.5s (Largest Contentful Paint)
- FID < 100ms (First Input Delay)
- CLS < 0.1 (Cumulative Layout Shift)
- Total page weight < 1MB (18% of pages over 1MB are abandoned by AI crawlers)

Verify: SSR or SSG (critical — AI crawlers often skip JS rendering), gzip or brotli compression, appropriate cache headers, lazy-loaded below-fold images (`loading="lazy"`), modern image formats (WebP/AVIF with `<picture>` fallbacks), HTTPS enforced, mobile-responsive.

### Step 9: Audit Content Patterns

Check whether the site's content templates implement high-citation patterns:

**Citable paragraph pattern** (every major claim should follow):
```
[Direct statement of fact]. [Specific statistic with attribution].
[Brief elaboration]. [Source: Named Organization, Date]
```

**FAQ block pattern** (at bottom of content pages):
- `<h2>` or `<h3>` with the exact question text
- 40-60 word direct answer immediately following
- FAQPage schema wrapping the section

**Definition block pattern** (for defining terms):
```html
<section id="what-is-term">
  <h2>What is [Term]?</h2>
  <p><dfn>[Term]</dfn> is [direct 1-sentence definition]. [Elaboration]. [Attribution].</p>
</section>
```

**Author attribution** (every content page):
- Visible author name and credentials
- Link to author profile page with Person schema, photo, bio, credentials, external profile links
- Content with proper author metadata receives 40% more AI citations

**Content length**: pages over 2,900 words are 59% more likely to be cited. Original or proprietary data generates 4.31× more citations per URL.

### Step 10: Check llms.txt (Emerging Standard)

Verify `/llms.txt` exists — a Markdown-formatted file describing the site for AI systems:

```markdown
# Site Name

> One-sentence description of what this site/organization does.

## Key Pages

- [About Us](https://yoursite.com/about): Description
- [Platform](https://yoursite.com/platform): What it does

## Key Facts

- Founded: [year]
- Type: [nonprofit/etc.]
- Focus: [primary mission]
```

Current status: Google says it has no value for their systems; no AI bots currently request it. Cloudflare and several platforms have adopted it. Low effort, uncertain current value, may become significant. Implement if the project has capacity.

### Step 11: Findings Report

Document findings organized by priority:

**Critical (blocks launch)**
- Primary content rendered JavaScript-only
- Missing `<h1>` or broken heading hierarchy
- Missing canonical tags (risks duplicate content penalty)
- robots.txt blocking AI citation crawlers
- Missing HTTPS

**High (implement before significant content investment)**
- Missing structured data (JSON-LD schema) — highest-leverage GEO action
- Missing FAQ schema on Q&A content
- Siloed content (no topic cluster architecture)
- Pages not server-side rendered or statically generated
- LCP > 2.5s or page weight > 1MB

**Medium (implement in next sprint)**
- Question-format headings not used
- Answer-first paragraph pattern not followed
- Missing author attribution
- Missing IndexNow integration
- Outdated or missing `dateModified` values

**Low (optimize over time)**
- `llms.txt` not implemented
- Individual content pieces not following citable paragraph pattern
- Missing comparison tables on decision-relevant pages

For each finding, provide: the specific page or component affected, what is missing or incorrect, and the exact implementation needed.
