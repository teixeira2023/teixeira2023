import os
from datetime import datetime

def generate_empty_feature(filename=None, feature_name=None, description=None):
    """
    Generate an empty .feature file with basic BDD structure.
    
    Args:
        filename (str): Name of the feature file (without .feature extension)
        feature_name (str): Name of the feature
        description (str): Description of the feature
    """
    
    # Default values if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"feature_{timestamp}"
    
    if feature_name is None:
        feature_name = "Sample Feature"
    
    if description is None:
        description = "This is a sample feature description"
    
    # Ensure filename has .feature extension
    if not filename.endswith('.feature'):
        filename += '.feature'
    
    # Basic BDD feature structure
    feature_content = f"""Feature: {feature_name}
  {description}

  Scenario: Basic scenario
    Given some precondition
    When some action is performed
    Then some expected result should occur

  Scenario Outline: Example scenario with examples
    Given a user with <user_type>
    When they perform <action>
    Then they should see <result>

    Examples:
      | user_type | action    | result           |
      | admin     | login     | dashboard access |
      | user      | register  | welcome message  |

"""
    
    # Write the feature file
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(feature_content)
        
        print(f"✅ Feature file created successfully: {filename}")
        print(f"📁 Location: {os.path.abspath(filename)}")
        print(f"📄 Feature name: {feature_name}")
        
        return filename
        
    except Exception as e:
        print(f"❌ Error creating feature file: {e}")
        return None

def generate_custom_feature(filename, scenarios=None):
    """
    Generate a custom feature file with user-defined scenarios.
    
    Args:
        filename (str): Name of the feature file
        scenarios (list): List of scenario dictionaries
    """
    
    if scenarios is None:
        scenarios = [
            {
                "name": "First scenario",
                "given": "I am on the login page",
                "when": "I enter valid credentials",
                "then": "I should be logged in successfully"
            },
            {
                "name": "Second scenario", 
                "given": "I am logged in",
                "when": "I click the logout button",
                "then": "I should be logged out"
            }
        ]
    
    # Ensure filename has .feature extension
    if not filename.endswith('.feature'):
        filename += '.feature'
    
    feature_content = f"""Feature: Custom Feature
  As a user
  I want to perform various actions
  So that I can test the application functionality

"""
    
    # Add scenarios
    for i, scenario in enumerate(scenarios, 1):
        feature_content += f"""  Scenario {i}: {scenario.get('name', f'Scenario {i}')}
    Given {scenario.get('given', 'some precondition')}
    When {scenario.get('when', 'some action is performed')}
    Then {scenario.get('then', 'some expected result should occur')}

"""
    
    # Write the feature file
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(feature_content)
        
        print(f"✅ Custom feature file created successfully: {filename}")
        print(f"📁 Location: {os.path.abspath(filename)}")
        print(f"📊 Number of scenarios: {len(scenarios)}")
        
        return filename
        
    except Exception as e:
        print(f"❌ Error creating custom feature file: {e}")
        return None

def generate_feature_from_template(template_name="basic"):
    """
    Generate a feature file from predefined templates.
    
    Args:
        template_name (str): Name of the template to use
    """
    
    templates = {
        "basic": {
            "filename": "basic_feature.feature",
            "content": """Feature: Basic Feature
  As a user
  I want to perform basic actions
  So that I can test the system

  Scenario: Basic functionality test
    Given I am on the application
    When I perform a basic action
    Then I should see the expected result
"""
        },
        "login": {
            "filename": "login_feature.feature", 
            "content": """Feature: User Authentication
  As a user
  I want to log in to the system
  So that I can access my account

  Background:
    Given I am on the login page

  Scenario: Successful login with valid credentials
    When I enter valid username and password
    And I click the login button
    Then I should be logged in successfully
    And I should see the dashboard

  Scenario: Failed login with invalid credentials
    When I enter invalid username and password
    And I click the login button
    Then I should see an error message
    And I should remain on the login page

  Scenario Outline: Login with different user types
    When I login as a <user_type>
    Then I should have <access_level> access

    Examples:
      | user_type | access_level |
      | admin     | full         |
      | user      | limited      |
      | guest     | read-only    |
"""
        },
        "api": {
            "filename": "api_feature.feature",
            "content": """Feature: API Testing
  As a developer
  I want to test API endpoints
  So that I can ensure they work correctly

  Scenario: GET request to retrieve data
    Given I have a valid API endpoint
    When I send a GET request
    Then I should receive a 200 status code
    And the response should contain valid data

  Scenario: POST request to create data
    Given I have valid data to send
    When I send a POST request with the data
    Then I should receive a 201 status code
    And the data should be created successfully
"""
        }
    }
    
    if template_name not in templates:
        print(f"❌ Template '{template_name}' not found. Available templates: {list(templates.keys())}")
        return None
    
    template = templates[template_name]
    
    try:
        with open(template["filename"], 'w', encoding='utf-8') as f:
            f.write(template["content"])
        
        print(f"✅ Feature file created from template '{template_name}': {template['filename']}")
        print(f"📁 Location: {os.path.abspath(template['filename'])}")
        
        return template["filename"]
        
    except Exception as e:
        print(f"❌ Error creating feature file from template: {e}")
        return None

if __name__ == "__main__":
    print("🚀 Feature File Generator")
    print("=" * 50)
    
    # Generate basic empty feature
    print("\n1. Generating basic empty feature file...")
    generate_empty_feature()
    
    # Generate custom feature
    print("\n2. Generating custom feature file...")
    custom_scenarios = [
        {
            "name": "User registration",
            "given": "I am on the registration page",
            "when": "I fill in all required fields",
            "then": "I should be registered successfully"
        },
        {
            "name": "Password reset",
            "given": "I am on the password reset page", 
            "when": "I enter my email address",
            "then": "I should receive a reset link"
        }
    ]
    generate_custom_feature("custom_user_actions", custom_scenarios)
    
    # Generate from templates
    print("\n3. Generating feature files from templates...")
    generate_feature_from_template("login")
    generate_feature_from_template("api")
    
    print("\n✅ All feature files generated successfully!")
    print("\n📋 Available templates: basic, login, api")
    print("💡 You can also create custom features with your own scenarios") 