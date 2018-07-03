# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gaipa.backend -t test_solutionservices.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gaipa.backend.testing.GAIPA_BACKEND_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/gaipa/backend/tests/robot/test_solutionservices.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a SolutionServices
  Given a logged-in site administrator
    and an add GaipaContent form
   When I type 'My SolutionServices' into the title field
    and I submit the form
   Then a SolutionServices with the title 'My SolutionServices' has been created

Scenario: As a site administrator I can view a SolutionServices
  Given a logged-in site administrator
    and a SolutionServices 'My SolutionServices'
   When I go to the SolutionServices view
   Then I can see the SolutionServices title 'My SolutionServices'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add GaipaContent form
  Go To  ${PLONE_URL}/++add++GaipaContent

a SolutionServices 'My SolutionServices'
  Create content  type=GaipaContent  id=my-solutionservices  title=My SolutionServices

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the SolutionServices view
  Go To  ${PLONE_URL}/my-solutionservices
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a SolutionServices with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the SolutionServices title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
