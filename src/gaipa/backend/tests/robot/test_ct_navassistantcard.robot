# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gaipa.backend -t test_navassistantcard.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gaipa.backend.testing.GAIPA_BACKEND_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/gaipa/backend/tests/robot/test_navassistantcard.robot
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

Scenario: As a site administrator I can add a NavAssistantCard
  Given a logged-in site administrator
    and an add NavAssistantCards form
   When I type 'My NavAssistantCard' into the title field
    and I submit the form
   Then a NavAssistantCard with the title 'My NavAssistantCard' has been created

Scenario: As a site administrator I can view a NavAssistantCard
  Given a logged-in site administrator
    and a NavAssistantCard 'My NavAssistantCard'
   When I go to the NavAssistantCard view
   Then I can see the NavAssistantCard title 'My NavAssistantCard'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add NavAssistantCards form
  Go To  ${PLONE_URL}/++add++NavAssistantCards

a NavAssistantCard 'My NavAssistantCard'
  Create content  type=NavAssistantCards  id=my-navassistantcard  title=My NavAssistantCard

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the NavAssistantCard view
  Go To  ${PLONE_URL}/my-navassistantcard
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a NavAssistantCard with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the NavAssistantCard title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
