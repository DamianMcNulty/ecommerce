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

  // it('can take a screenshot', function(){
  //   cy.screenshot('site', {capture: 'runner'});
  // });

});