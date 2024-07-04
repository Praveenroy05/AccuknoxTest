const {test} = require('@playwright/test');


test("Message validation",async ({page}) => {

  const frontendUrl = 'http://127.0.0.1:54709'; // Replace with actual URL

    try {
        await page.goto(frontendUrl);
        const content = await page.textContent('h1');

        if (content.includes('Hello from the Backend!')) {
            console.log('Test passed: Frontend displayed the correct message.');
        } else {
            console.log('Test failed: Frontend did not display the correct message.');
        }
    } catch (error) {
        console.error('Test failed: Could not access frontend service.', error);
    }

    await page.close();
})
