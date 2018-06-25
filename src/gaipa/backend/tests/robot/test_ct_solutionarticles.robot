# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gaipa.backend -t test_solutionarticles.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gaipa.backend.testing.GAIPA_BACKEND_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/gaipa/backend/tests/robot/test_solutionarticles.robot
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

Scenario: As a site administrator I can add a SolutionArticles
  Given a logged-in site administrator
    and an add GaipaContent form
   When I type 'My SolutionArticles' into the title field
    and I submit the form
   Then a SolutionArticles with the title 'My SolutionArticles' has been created

Scenario: As a site administrator I can view a SolutionArticles
  Given a logged-in site administrator
    and a SolutionArticles 'My SolutionArticles'
   When I go to the SolutionArticles view
   Then I can see the SolutionArticles title 'My SolutionArticles'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add GaipaContent form
  Go To  ${PLONE_URL}/++add++GaipaContent

a SolutionArticles 'My SolutionArticles'
  Create content  type=GaipaContent  id=my-solutionarticles  title=My SolutionArticles

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the SolutionArticles view
  Go To  ${PLONE_URL}/my-solutionarticles
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a SolutionArticles with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the SolutionArticles title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
