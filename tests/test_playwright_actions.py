

def test_checkboxes(actions_driver):
    page = actions_driver
    page.get_by_role("link", name="Checkboxes").click()
    # checkbox_1 = page.get_by_role("checkbox").first
    checkbox_1 = page.locator('css=[type="checkbox"]:nth-child(1)')  # Test find locator by css selector
    checkbox_2 = page.get_by_role("checkbox").nth(1)  # Test find locator by codegen
    checkbox_1.check()
    checkbox_2.uncheck()

    # expect(checkbox_1).to_be_checked()  # Playwright default assertion
    # expect(checkbox_2).not_to_be_checked()  # # Playwright default assertion

    assert checkbox_1.is_checked()
    assert not checkbox_2.is_checked()

