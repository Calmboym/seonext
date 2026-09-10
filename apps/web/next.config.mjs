/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // packages/ui (PHASE-0.6) ships raw TypeScript source with no build
  // step of its own — Next transpiles it directly rather than requiring
  // packages/ui to maintain its own bundler config, matching this
  // subtask's "empty-but-wired" scope (.ai/WBS.md §4).
  transpilePackages: ["@seonex/ui"],
};

export default nextConfig;
