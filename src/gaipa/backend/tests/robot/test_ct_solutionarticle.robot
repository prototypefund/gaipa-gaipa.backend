# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gaipa.backend -t test_solutionarticle.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gaipa.backend.testing.GAIPA_BACKEND_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/gaipa/backend/tests/robot/test_solutionarticle.robot
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

Scenario: As a site administrator I can add a SolutionArticle
  Given a logged-in site administrator
    and an add SolutionArticles form
   When I type 'My SolutionArticle' into the title field
    and I submit the form
   Then a SolutionArticle with the title 'My SolutionArticle' has been created

Scenario: As a site administrator I can view a SolutionArticle
  Given a logged-in site administrator
    and a SolutionArticle 'My SolutionArticle'
   When I go to the SolutionArticle view
   Then I can see the SolutionArticle title 'My SolutionArticle'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add SolutionArticles form
  Go To  ${PLONE_URL}/++add++SolutionArticles

a SolutionArticle 'My SolutionArticle'
  Create content  type=SolutionArticles  id=my-solutionarticle  title=My SolutionArticle

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the SolutionArticle view
  Go To  ${PLONE_URL}/my-solutionarticle
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a SolutionArticle with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the SolutionArticle title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
