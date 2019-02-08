describe('homepage', function() {
  beforeEach(function() {
    cy.visit('/');
  });

  it('get the title', function(){
    cy.title().should('include', 'Issue Tracker')
  });

  it('click on Visualisations', () => {
    cy.get('.Visualisations__link').click();
  });

  it('click on Rank', () => {
    cy.get('.Rank__link').click();
  });

  it('click on Bugs', () => {
    cy.get('.Bugs__link').click();
  });

  it('click on Register', () => {
    cy.get('.Register__link').click();
  });

  it('click on Login', () => {
    cy.get('.Login__link').click();
  });

  it('creates a new account', function(){
    cy.contains('Register').click();
    cy.get('#id_username')
      .type('D1')
      .should('have.value', 'D1');
    cy.get('#id_email')
      .type('d1@me.com')
      .should('have.value', 'd1@me.com');
    cy.get('#id_password1')
      .type('password')
      .should('have.value', 'password');
    cy.get('#id_password2')
      .type('password')
      .should('have.value', 'password');
    cy.get('.CreateAccount__button').click();
    cy.get('.Logout__button').click();
  });

  it('contains "Login"', function(){
    cy.contains('Log In').click();
    cy.get('#id_username_or_email')
      .type('D1')
      .should('have.value', 'D1');
    cy.get('#id_password')
      .type('password')
      .should('have.value', 'password');
    cy.get('.Login__button').click();
    cy.get('.Logout__button').click();
  });

  // it('can take a screenshot', function(){
  //   cy.screenshot('site', {capture: 'runner'});
  // });

});