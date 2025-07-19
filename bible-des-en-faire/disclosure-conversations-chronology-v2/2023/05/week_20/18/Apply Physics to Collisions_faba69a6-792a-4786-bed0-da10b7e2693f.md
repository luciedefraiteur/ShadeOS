# Apply Physics to Collisions

**Date de création :** 2023-05-18 14:45:48

---

**Lucie :**
After retrieving an array of collisions in 3d in typescript as { penetrationDepth: number, penetrationNormal: Vector3 }[] how can i apply physics to my object

---

**Lucie :**
Can you give details of each methods you provided in your code

---

**Lucie :**
Can you give code for calculate resolutionImpulse and applyImpulse, knowing that my rigidbody is a capsule representing character

---

**Lucie :**
Can you add something to handle gravity and to prevent my character to fall through the ground

---

**Lucie :**
Add to this code a logic to handle gravity:

class PhysicsObject {
  // ...
applyCollision(collisions: Collision[]) {
    for (const collision of collisions) {
      const resolutionImpulse = calculateResolutionImpulse(collision.penetrationDepth, collision.penetrationNormal);
      this.applyImpulse(resolutionImpulse);
    }
  }
  calculateResolutionImpulse(penetrationDepth: number, penetrationNormal: Vector3): Vector3 {
    const restitution = 0.5; // Coefficient of restitution (bounce factor)
    const velocityAlongNormal = this.velocity.x * penetrationNormal.x +
                                this.velocity.y * penetrationNormal.y +
                                this.velocity.z * penetrationNormal.z;
    const impulseMagnitude = -(1 + restitution) * velocityAlongNormal;

    const impulse = {
      x: impulseMagnitude * penetrationNormal.x,
      y: impulseMagnitude * penetrationNormal.y,
      z: impulseMagnitude * penetrationNormal.z
    };

    return impulse;
  }

  applyImpulse(impulse: Vector3) {
    // Apply the impulse to the object's velocity
    this.velocity.x += impulse.x;
    this.velocity.y += impulse.y;
    this.velocity.z += impulse.z;
  }
}

// Usage example
const object = new PhysicsObject();
// ...

---

**Lucie :**
can you describe full detailed pseudocode of that function:

World.prototype.step = function(dt, timeSinceLastCalled, maxSubSteps)

from the git https://schteppe.github.io/cannon.js/
