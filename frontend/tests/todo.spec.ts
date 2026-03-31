import { test, expect } from '@playwright/test';

test('todoを追加すると一覧に表示される', async ({ page }) => {
  const title = `Playwright学習-${Date.now()}`;

  await page.goto('http://127.0.0.1:3000');

  await page.getByPlaceholder('Todo title').fill(title);
  await page.getByRole('button', { name: '追加' }).click();

  await expect(page.getByText(title)).toBeVisible();
});