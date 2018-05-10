from ..po import Reset_element

class CreatPage(Reset_element.Reset):
    found_clock =('com.philliphsu.clock2.debug:id/fab')

    def run_case(self):
        self.find_element(self.found_clock).click()