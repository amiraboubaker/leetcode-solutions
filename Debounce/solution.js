// Intuition
// Calling the function immediately every time defeats the purpose.
// The idea is simple: **delay execution** by `t` milliseconds, and if another call happens before that delay ends, cancel the previous one and start over.
// Only the **last call in a burst** should survive.
// This means we need:
// - A timer we can cancel.
// - A way to remember the latest arguments.
// Classic debounce behavior. Nothing mystical.

// Approach
// 1. Keep a `timer` variable in the closure.
// 2. When the debounced function is called:
//    - Cancel any existing timer.
//    - Store the latest arguments.
//    - Start a new timer that will call `fn` after `t` milliseconds with the latest arguments.
// 3. If no new call interrupts the timer, the function finally executes.

// Complexity
// - Time complexity:
//   $$O(1)$$ per call
// - Space complexity:
//   $$O(1)$$
//   Only one timer and argument reference are stored.

// Code
var debounce = function (fn, t) {
    let timer = null;

    return function (...args) {
        if (timer !== null) {
            clearTimeout(timer);
        }

        timer = setTimeout(() => {
            fn(...args);
        }, t);
    };
};

module.exports = { debounce };