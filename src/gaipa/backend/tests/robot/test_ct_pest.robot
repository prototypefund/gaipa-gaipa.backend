# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gaipa.backend -t test_pest.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gaipa.backend.testing.GAIPA_BACKEND_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/gaipa/backend/tests/robot/test_pest.robot
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

Scenario: As a site administrator I can add a Pest
  Given a logged-in site administrator
    and an add Pests form
   When I type 'My Pest' into the title field
    and I submit the form
   Then a Pest with the title 'My Pest' has been created

Scenario: As a site administrator I can view a Pest
  Given a logged-in site administrator
    and a Pest 'My Pest'
   When I go to the Pest view
   Then I can see the Pest title 'My Pest'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Pests form
  Go To  ${PLONE_URL}/++add++Pests

a Pest 'My Pest'
  Create content  type=Pests  id=my-pest  title=My Pest

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Pest view
  Go To  ${PLONE_URL}/my-pest
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Pest with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Pest title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
