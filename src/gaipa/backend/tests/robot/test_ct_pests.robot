# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gaipa.backend -t test_pests.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gaipa.backend.testing.GAIPA_BACKEND_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/gaipa/backend/tests/robot/test_pests.robot
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

Scenario: As a site administrator I can add a Pests
  Given a logged-in site administrator
    and an add Pests form
   When I type 'My Pests' into the title field
    and I submit the form
   Then a Pests with the title 'My Pests' has been created

Scenario: As a site administrator I can view a Pests
  Given a logged-in site administrator
    and a Pests 'My Pests'
   When I go to the Pests view
   Then I can see the Pests title 'My Pests'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Pests form
  Go To  ${PLONE_URL}/++add++Pests

a Pests 'My Pests'
  Create content  type=Pests  id=my-pests  title=My Pests

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Pests view
  Go To  ${PLONE_URL}/my-pests
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Pests with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Pests title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
