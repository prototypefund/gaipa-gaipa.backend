# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gaipa.backend -t test_crop.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gaipa.backend.testing.GAIPA_BACKEND_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/gaipa/backend/tests/robot/test_crop.robot
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

Scenario: As a site administrator I can add a Crop
  Given a logged-in site administrator
    and an add CropContainer form
   When I type 'My Crop' into the title field
    and I submit the form
   Then a Crop with the title 'My Crop' has been created

Scenario: As a site administrator I can view a Crop
  Given a logged-in site administrator
    and a Crop 'My Crop'
   When I go to the Crop view
   Then I can see the Crop title 'My Crop'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add CropContainer form
  Go To  ${PLONE_URL}/++add++CropContainer

a Crop 'My Crop'
  Create content  type=CropContainer  id=my-crop  title=My Crop

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Crop view
  Go To  ${PLONE_URL}/my-crop
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Crop with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Crop title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
