# GEO + SEO Audit for Advocacy Websites

You are running a GEO + SEO audit on an animal advocacy website. GEO (Generative Engine Optimization) ensures content appears in AI answer systems — ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini, Bing Copilot. Approximately 60% of searches end without a click; AI systems are the fastest-growing discovery channel. Follow these steps in order.

## Step 1: Audit HTML Structure

Check every page for exactly one `<h1>` tag, logical heading hierarchy with no skipped levels, and `<h2>` headings phrased as questions (7× more AI citations for smaller sites). Verify the first paragraph after each heading answers the question directly in 40-60 words — AI systems pull from the first 30% of content 44% of the time. Check paragraphs are 2-4 sentences (40-60 words) and content sections are self-contained 120-180 word modules (70% more ChatGPT citations). Verify semantic HTML (`<article>`, `<section>`, `<main>`, etc.), `lang` attribute on `<html>`, descriptive `alt` text on all images, and meaningful anchor text on all links. Flag any primary content rendered exclusively by JavaScript — AI crawlers often skip JS rendering.

## Step 2: Audit Structured Data (JSON-LD)

Structured data is the single highest-leverage GEO action: 41% citation rate with schema vs 15% without. Verify Organization + WebSite schema on every page (in a `@graph` array). Verify Article schema on every content page with `headline`, `author` (name, url, jobTitle), `publisher`, `datePublished`, `dateModified`, `image`, `description`. Verify FAQPage schema on any page with Q&A content. Check whether HowTo, BreadcrumbList, SoftwareApplication, Event, Dataset, or Person schema applies. Validate all schema at schema.org/validator. Confirm `dateModified` reflects actual update dates.

## Step 3: Audit Meta Tags

For every page: `<title>` must be `Primary Keyword — Brand Name`, 50-60 chars, keywords first, unique per page. `<meta name="description">` must be 150-160 chars, a direct factual answer to the primary query with one specific statistic, never duplicated across pages. Verify `<link rel="canonical">`. Verify all Open Graph tags (`og:title`, `og:description`, `og:type`, `og:url`, `og:image`, `og:site_name`). Verify Twitter Card tags. Verify article timestamp tags in ISO 8601 format.

## Step 4: Audit robots.txt

Verify AI citation crawlers are allowed: `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `ClaudeBot`, `Claude-SearchBot`, `Applebot`, `Amazonbot`. These power AI answer systems — blocking them eliminates AI visibility. Verify the `Sitemap:` directive points to the correct URL. Note: blocking `Googlebot` blocks both Google Search AND Google AI Overviews.

## Step 5: Audit XML Sitemap and IndexNow

Verify the sitemap exists at `/sitemap.xml`, contains only canonical indexable URLs, and `<lastmod>` dates reflect actual content update dates. Verify the sitemap is submitted to Google Search Console and Bing Webmaster Tools. Check whether IndexNow is integrated — it notifies Bing (which feeds ChatGPT) instantly on publish, dramatically accelerating AI discovery.

## Step 6: Audit Site Architecture

Verify URLs are descriptive, hyphenated, lowercase, under 75 characters, and at most 3 levels deep. Verify canonical tags on every page. Assess whether the site uses a hub-and-spoke topic cluster model — a pillar page (2,000-4,000 words) supported by 8-15 cluster pages with bidirectional links — which increases AI citation rate from 12% to 41%. Verify "Last Updated" dates are visible using `<time datetime="YYYY-MM-DD">` and synchronized with `dateModified` in schema.

## Step 7: Audit Performance

AI crawlers timeout at 1-5 seconds. Verify TTFB < 200ms, LCP < 2.5s, CLS < 0.1, page weight < 1MB. Verify SSR or SSG (AI crawlers skip JS rendering). Verify HTTPS, gzip/brotli compression, appropriate cache headers, and modern image formats.

## Step 8: Audit Content Patterns

Check whether content follows citable paragraph pattern: direct statement of fact, specific statistic with attribution, brief elaboration, source citation. Check for FAQ blocks with question-format headings and 40-60 word direct answers. Check for definition blocks using `<dfn>`. Check for visible author attribution with credentials and links to author profile pages with Person schema — proper author metadata increases AI citations by 40%.

## Step 9: Findings Report

Document findings by priority:
- **Critical** — JS-only primary content, broken heading hierarchy, robots.txt blocking AI crawlers, missing HTTPS
- **High** — missing structured data (highest-leverage action), no FAQ schema, siloed content, no SSR/SSG
- **Medium** — headings not question-format, no answer-first paragraphs, missing author attribution, missing IndexNow
- **Low** — no `llms.txt`, content not following citable paragraph pattern, missing comparison tables

For each finding: the specific page or component affected, what is missing or incorrect, and the exact implementation needed.
