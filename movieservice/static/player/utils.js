/*
MIT License

Copyright (c) 2024 Kirills Reunovs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/
// Logging utility
const logger = {
    info: (...args) => console.info('[Tape Operator Player]', ...args),
    warn: (...args) => console.warn('[Tape Operator Player]', ...args),
    error: (...args) => console.error('[Tape Operator Player]', ...args),
}

/**
 * Returns a hash code from a string
 * @param {string} str The string to hash
 * @return {number} A 32bit integer
 */
function hashCode(str) {
    let hash = 0;

    for (let i = 0, len = str.length; i < len; i++) {
        hash = (hash << 5) - hash + str.charCodeAt(i);
        hash |= 0;
    }

    return Math.abs(hash);
}

/**
 * Update URL by setting a search parameter
 * @param {string} key
 * @param {string} value
 */
function setSearchParam(key, value) {
    const url = new URL(location.href);
    url.searchParams.set(key, value);
    history.replaceState(null, '', url.toString());
}

/**
 * Get search parameter from URL
 * @param {string} key
 * @return {string}
 */
function getSearchParam(key) {
    const url = new URL(location.href);
    return url.searchParams.get(key);
}

/**
 * Parse a version string into a number
 */
function parseVersion(version) {
    return parseInt(version.replace(/\D/g, ''));
}