from tests.integration.test_base import BaseIntegrationTest


class TestDragAndDropRender(BaseIntegrationTest):
    """
    Verifying Drag and Drop XBlock rendering against default data - if default data changes this would probably broke
    """
    PAGE_TITLE = 'Drag and Drop v2'
    PAGE_ID = 'drag_and_drop_v2'
    
    def setUp(self):
        super(TestDragAndDropRender, self).setUp()

        scenario_xml = "<vertical_demo><drag-and-drop-v2/></vertical_demo>"
        self._add_scenario(self.PAGE_ID, self.PAGE_TITLE, scenario_xml)

        self.browser.get(self.live_server_url)
        self._page = self.go_to_page(self.PAGE_TITLE)

    def _get_items(self):
        items_container = self._page.find_element_by_css_selector('ul.items')
        return items_container.find_elements_by_css_selector('li.option')

    def _get_zones(self):
        return self._page.find_elements_by_css_selector(".drag-container .zone")



    def test_items(self):
        items = self._get_items()

        self.assertEqual(len(items), 3)

        self.assertEqual(items[0].get_attribute('data-value'), '0')
        self.assertEqual(items[0].text, 'A')
        self.assertEqual(items[0].get_attribute('style'), u"width: 190px; height: auto;")
        self.assertIn('ui-draggable', self.get_element_classes(items[0]))

        self.assertEqual(items[1].get_attribute('data-value'), '1')
        self.assertEqual(items[1].text, 'B')
        self.assertEqual(items[1].get_attribute('style'), u"width: 190px; height: auto;")
        self.assertIn('ui-draggable', self.get_element_classes(items[1]))

        self.assertEqual(items[2].get_attribute('data-value'), '2')
        self.assertEqual(items[2].text, 'X')
        self.assertEqual(items[2].get_attribute('style'), u"width: 100px; height: 100px;")
        self.assertIn('ui-draggable', self.get_element_classes(items[2]))

    def test_zones(self):
        zones = self._get_zones()

        self.assertEqual(len(zones), 2)

        self.assertEqual(zones[0].get_attribute('data-zone'), 'Zone A')
        self.assertEqual(zones[0].get_attribute('style'), u"top: 200px; left: 120px; width: 200px; height: 100px;")
        self.assertIn('ui-droppable', self.get_element_classes(zones[0]))

        self.assertEqual(zones[1].get_attribute('data-zone'), 'Zone B')
        self.assertEqual(zones[1].get_attribute('style'), u"top: 360px; left: 120px; width: 200px; height: 100px;")
        self.assertIn('ui-droppable', self.get_element_classes(zones[1]))

    def test_feedback(self):
        feedback_message = self._get_feedback_message()

        self.assertEqual(feedback_message.text, "Intro Feed")