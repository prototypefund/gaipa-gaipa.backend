# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gaipa.backend -t test_crop_container.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gaipa.backend.testing.GAIPA_BACKEND_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/gaipa/backend/tests/robot/test_crop_container.robot
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

Scenario: As a site administrator I can add a CropContainer
  Given a logged-in site administrator
    and an add CropContainer form
   When I type 'My CropContainer' into the title field
    and I submit the form
   Then a CropContainer with the title 'My CropContainer' has been created

Scenario: As a site administrator I can view a CropContainer
  Given a logged-in site administrator
    and a CropContainer 'My CropContainer'
   When I go to the CropContainer view
   Then I can see the CropContainer title 'My CropContainer'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add CropContainer form
  Go To  ${PLONE_URL}/++add++CropContainer

a CropContainer 'My CropContainer'
  Create content  type=CropContainer  id=my-crop_container  title=My CropContainer

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the CropContainer view
  Go To  ${PLONE_URL}/my-crop_container
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a CropContainer with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the CropContainer title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
