# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gaipa.backend -t test_solutionprovider.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gaipa.backend.testing.GAIPA_BACKEND_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/gaipa/backend/tests/robot/test_solutionprovider.robot
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

Scenario: As a site administrator I can add a SolutionProvider
  Given a logged-in site administrator
    and an add SolutionProviders form
   When I type 'My SolutionProvider' into the title field
    and I submit the form
   Then a SolutionProvider with the title 'My SolutionProvider' has been created

Scenario: As a site administrator I can view a SolutionProvider
  Given a logged-in site administrator
    and a SolutionProvider 'My SolutionProvider'
   When I go to the SolutionProvider view
   Then I can see the SolutionProvider title 'My SolutionProvider'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add SolutionProviders form
  Go To  ${PLONE_URL}/++add++SolutionProviders

a SolutionProvider 'My SolutionProvider'
  Create content  type=SolutionProviders  id=my-solutionprovider  title=My SolutionProvider

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the SolutionProvider view
  Go To  ${PLONE_URL}/my-solutionprovider
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a SolutionProvider with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the SolutionProvider title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
