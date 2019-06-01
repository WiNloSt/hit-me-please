describe('Landing page', () => {
  it('submit form with email', () => {
    cy.visit('http://localhost:8000/admin')
    cy.getByLabelText('Username:')
      .type(Cypress.env('username'))
      .getByLabelText('Password:')
      .type(Cypress.env('password'))

    cy.contains('Log in').click()

    cy.get('tbody')
      .contains('Hitters')
      .click()

    cy.contains('kelvin@prontomarketing.com').should('be.visible')
  })
})
