# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gaipa.backend -t test_solution_service.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gaipa.backend.testing.GAIPA_BACKEND_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/gaipa/backend/tests/robot/test_solution_service.robot
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

Scenario: As a site administrator I can add a Solution Service
  Given a logged-in site administrator
    and an add SolutionServices form
   When I type 'My Solution Service' into the title field
    and I submit the form
   Then a Solution Service with the title 'My Solution Service' has been created

Scenario: As a site administrator I can view a Solution Service
  Given a logged-in site administrator
    and a Solution Service 'My Solution Service'
   When I go to the Solution Service view
   Then I can see the Solution Service title 'My Solution Service'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add SolutionServices form
  Go To  ${PLONE_URL}/++add++SolutionServices

a Solution Service 'My Solution Service'
  Create content  type=SolutionServices  id=my-solution_service  title=My Solution Service

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Solution Service view
  Go To  ${PLONE_URL}/my-solution_service
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Solution Service with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Solution Service title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
