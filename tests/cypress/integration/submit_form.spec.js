describe('Landing page', () => {
  after(() => {
    deleteAllHitters()
  })

  it('save hitters', () => {
    const email = 'kelvin@prontomarketing.com'
    cy.visit('http://localhost:8000')

    cy.getByLabelText('Email:').type(email)
    cy.contains('Submit').click()

    assertEmailIsSaved(email)
  })
})

function assertEmailIsSaved(email) {
  login()

  cy.get('tbody')
    .contains('Hitters')
    .click()
  cy.contains(email).should('be.visible')
}

function login() {
  cy.visit('http://localhost:8000/admin')
  cy.getByLabelText('Username:')
    .type(Cypress.env('username'))
    .getByLabelText('Password:')
    .type(Cypress.env('password'))
  cy.contains('Log in').click()
}

function deleteAllHitters() {
  cy.get('#action-toggle').click()
  cy.get('select[name=action]').select('delete_selected')

  cy.contains('Go').click()

  cy.contains(`Yes, I'm sure`).click()
}
