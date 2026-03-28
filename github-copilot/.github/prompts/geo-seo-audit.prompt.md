# GEO + SEO Audit for Advocacy Websites

You are running a comprehensive SEO + GEO audit on an animal advocacy website. GEO (Generative Engine Optimization) ensures content appears in AI answer systems — ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini, Bing Copilot. Approximately 60% of searches end without a click; AI systems are the fastest-growing discovery channel. Follow these steps in order.

## Step 1: Audit HTML Structure

Check every page for exactly one `<h1>` tag, logical heading hierarchy with no skipped levels, and `<h2>` headings phrased as questions (7× more AI citations for smaller sites). Verify the first paragraph after each heading answers the question directly in 40-60 words — AI systems pull from the first 30% of content 44% of the time. Check paragraphs are 2-4 sentences (40-60 words) and content sections are self-contained 120-180 word modules (70% more ChatGPT citations). Verify semantic HTML (`<article>`, `<section>`, `<main>`, etc.), `lang` attribute on `<html>`, descriptive `alt` text on all images with keyword-rich file names, and meaningful anchor text on all links. Flag any primary content rendered exclusively by JavaScript — AI crawlers skip JS rendering, and relying on it increases crawl cost for search engines.

## Step 2: Audit Semantic Writing Quality

AI citation systems retrieve at the sentence level, not the page level. Verify the primary entity appears as the grammatical subject in active voice — active voice gives salience 0.74; passive drops it to 0.11. Check that sentences are self-contained semantic triples (subject + verb + object with explicit context) — every sentence must make sense in isolation with no vague pronouns. Verify proper noun density is high (AI-cited text averages 20.6% proper nouns vs 5-8% standard). Check page character count: under 5,000 chars gets 66% of content used by AI; over 20,000 chars gets only 12%. Flag any vague attribution ("experts say") — specific named attribution always outperforms it.

## Step 3: Audit Structured Data (JSON-LD)

Structured data is the single highest-leverage GEO action: 41% citation rate with schema vs 15% without. Verify Organization + WebSite schema on every page (in a `@graph` array) with `sameAs` pointing to Wikipedia and Wikidata URLs. Verify Article schema on every content page with `headline`, `author` (name, url, jobTitle), `publisher`, `datePublished`, `dateModified`, `image`, `description`. Verify FAQPage schema on any page with Q&A content. Check whether HowTo, BreadcrumbList, Person, VideoObject, SoftwareApplication, Event, Dataset schema applies. Validate all schema at schema.org/validator. Confirm `dateModified` reflects actual update dates.

## Step 4: Audit Meta Tags

For every page: `<title>` must be `Primary Keyword — Brand Name`, 50-60 chars, keywords first, unique per page. `<meta name="description">` must be 150-160 chars, a direct factual answer to the primary query with one specific statistic, never duplicated across pages. Verify `<link rel="canonical">`. Verify all Open Graph tags. Verify Twitter Card tags. Verify article timestamp tags in ISO 8601 format.

## Step 5: Audit Wikipedia and Wikidata Presence

Wikipedia accounts for 47.9% of ChatGPT's top-10 cited sources. Verify: Does the organization have a Wikipedia article that is accurate, cited, and current? Does it have a Wikidata entry (Q-ID) with complete structured data — type, founding date, location, founders, official website, social profiles? Is the Wikidata Q-ID in the Organization schema `sameAs` array? Is the Wikipedia URL in `sameAs`? Is there an entity web connecting organization → tools → people → related organizations → policy areas? Are key facts (founding date, mission) consistent between the site's structured data and Wikipedia/Wikidata? If no Wikipedia article exists and sufficient third-party sources exist for notability, flag as High priority — creating the article outranks almost any on-site optimization.

## Step 6: Audit robots.txt

Verify AI citation crawlers are allowed: `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `ClaudeBot`, `Claude-SearchBot`, `Applebot`, `Amazonbot`. These power AI answer systems — blocking them eliminates AI visibility. Verify the `Sitemap:` directive is present. Note: blocking `Googlebot` blocks both Google Search AND Google AI Overviews — these cannot be separated.

## Step 7: Audit XML Sitemap and IndexNow

Verify the sitemap exists at `/sitemap.xml`, contains only canonical indexable URLs, `<lastmod>` dates reflect actual content update dates (never faked), and the file is under 50,000 URLs and 50MB. Verify submitted to Google Search Console and Bing Webmaster Tools. Check whether IndexNow is integrated — it notifies Bing (which feeds ChatGPT) instantly on publish.

## Step 8: Audit Site Architecture and Performance

Verify hub-and-spoke topic cluster model — pillar pages (2,000-4,000 words) supported by 8-15 cluster pages with bidirectional links — increases AI citation rate from 12% to 41%. Verify "Last Updated" dates visible via `<time datetime="YYYY-MM-DD">` synchronized with `dateModified`. Verify URLs descriptive, hyphenated, lowercase, max 3 levels deep.

Core Web Vitals (March 2026 thresholds): LCP ≤ 2.5s, INP ≤ 200ms (replaced FID), CLS ≤ 0.1. Verify SSR or SSG, HTTPS, gzip/brotli, `<link rel="preload">` for LCP element, explicit `width`/`height` on all images (CLS prevention), `loading="lazy"` for below-fold images, WebP/AVIF formats.

## Step 9: Audit Content Patterns and E-E-A-T

Check whether content follows citable paragraph pattern: direct statement + statistic with attribution + elaboration + source citation. Check for FAQ blocks with question-format headings and 40-60 word direct answers with FAQPage schema. Check for definition blocks using `<dfn>`. Verify E-E-A-T signals: original data or case studies (Experience), specific citations with named sources and dates (Expertise), clear contact info and organizational transparency (Trustworthiness). Verify visible author attribution on every content page with credentials and link to author profile page with Person schema — proper author metadata increases AI citations by 40%.

## Step 10: Audit Defensive and Risk Checks

Verify no content is hidden via `display:none`, `visibility:hidden`, white-on-white text, zero-size fonts, negative off-screen positioning, or invisible Unicode characters (U+E0000 to U+E007F). These techniques are explicitly prohibited by Google's spam policies and actively detected by tools like PhantomLint — penalties are domain-wide. Verify the server does not serve different content to AI crawlers vs human visitors based on User-Agent detection (agent-aware cloaking) — also explicitly prohibited with domain-wide penalty risk. Verify all published content has meaningful human review — Google issues manual actions for "scaled content abuse" since June 2025.

## Step 11: Findings Report

Document findings by priority:

- **Critical** — JS-only primary content, broken heading hierarchy, robots.txt blocking AI citation crawlers, missing HTTPS, agent-aware cloaking detected
- **High** — LCP > 2.5s (failing March 2026 threshold), missing structured data, no Wikipedia article when notability sources exist, no Wikidata entry, missing `sameAs` Wikipedia/Wikidata links, no topic cluster architecture
- **Medium** — headings not question-format, passive voice and weak entity salience, no answer-first paragraphs, missing author attribution with Person schema, missing IndexNow, outdated `dateModified` values, key facts inconsistent across platforms
- **Low** — no `llms.txt` (zero current AI value but low-effort), content not following citable paragraph pattern, missing VideoObject schema for video content

For each finding: the specific page or component affected, what is missing or incorrect, and the exact implementation needed.

