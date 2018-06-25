# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gaipa.backend -t test_navassistantcards.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gaipa.backend.testing.GAIPA_BACKEND_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/gaipa/backend/tests/robot/test_navassistantcards.robot
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

Scenario: As a site administrator I can add a NavAssistantCards
  Given a logged-in site administrator
    and an add GaipaContent form
   When I type 'My NavAssistantCards' into the title field
    and I submit the form
   Then a NavAssistantCards with the title 'My NavAssistantCards' has been created

Scenario: As a site administrator I can view a NavAssistantCards
  Given a logged-in site administrator
    and a NavAssistantCards 'My NavAssistantCards'
   When I go to the NavAssistantCards view
   Then I can see the NavAssistantCards title 'My NavAssistantCards'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add GaipaContent form
  Go To  ${PLONE_URL}/++add++GaipaContent

a NavAssistantCards 'My NavAssistantCards'
  Create content  type=GaipaContent  id=my-navassistantcards  title=My NavAssistantCards

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the NavAssistantCards view
  Go To  ${PLONE_URL}/my-navassistantcards
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a NavAssistantCards with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the NavAssistantCards title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
