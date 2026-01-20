const { debounce } = require('./solution');

function testDebounce() {
    let callCount = 0;
    const fn = () => callCount++;

    const debouncedFn = debounce(fn, 100);

    // Call multiple times quickly
    debouncedFn();
    debouncedFn();
    debouncedFn();

    // Wait for debounce
    setTimeout(() => {
        console.log('Call count after debounce:', callCount); // Should be 1
    }, 150);
}

testDebounce();